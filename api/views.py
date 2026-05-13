from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from articles.models import Article
from .serializers import ArticleSerializer


# GET all approved articles
@api_view(['GET'])
def approved_articles(request):
    articles = Article.objects.filter(approved=True)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


# GET subscribed articles
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subscribed_articles(request):
    user = request.user

    articles = Article.objects.filter(
        author__in=user.subscriptions.all(),
        approved=True
    )

    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


# GET single article
@api_view(['GET'])
def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


# POST article (journalist only)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article_api(request):
    if request.user.role != "journalist":
        return Response({"error": "Only journalists can create articles"})

    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)

    return Response(serializer.data)


# PUT update article
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.user.role not in ["journalist", "editor"]:
        return Response({"error": "Not allowed"})

    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# DELETE article
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.user.role not in ["journalist", "editor"]:
        return Response({"error": "Not allowed"})

    article.delete()
    return Response({"message": "Deleted"})
