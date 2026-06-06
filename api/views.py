from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
import requests

from articles.models import Article
from newsletters.models import Newsletter
from .serializers import ArticleSerializer, NewsletterSerializer


# =========================
# APPROVED ARTICLES
# =========================
@api_view(['GET'])
def approved_articles(request):
    articles = Article.objects.filter(approved=True)
    return Response(ArticleSerializer(articles, many=True).data)


# =========================
# SUBSCRIBED ARTICLES
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subscribed_articles(request):
    user = request.user

    articles = (
        Article.objects.filter(approved=True, author__in=user.subscribed_journalists.all())
        | Article.objects.filter(approved=True, publisher__in=user.subscribed_publishers.all())
    )

    return Response(ArticleSerializer(articles, many=True).data)


# =========================
# SINGLE ARTICLE
# =========================
@api_view(['GET'])
def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    return Response(ArticleSerializer(article).data)


# =========================
# CREATE ARTICLE
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article_api(request):

    if not request.user.groups.filter(name="Journalist").exists():
        return Response({"error": "Only journalists allowed"}, status=403)

    serializer = ArticleSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


# =========================
# UPDATE ARTICLE
# =========================
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_article(request, pk):

    article = get_object_or_404(Article, id=pk)

    if not request.user.groups.filter(name__in=["Journalist", "Editor"]).exists():
        return Response({"error": "Not allowed"}, status=403)

    serializer = ArticleSerializer(article, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# =========================
# DELETE ARTICLE
# =========================
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_article(request, pk):

    article = get_object_or_404(Article, id=pk)

    if not request.user.groups.filter(name__in=["Journalist", "Editor"]).exists():
        return Response({"error": "Not allowed"}, status=403)

    article.delete()
    return Response({"message": "Deleted"}, status=204)


# =========================
# APPROVAL (CRITICAL)
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def approve_article(request, pk):

    if not request.user.groups.filter(name="Editor").exists():
        return Response({"error": "Only editors can approve"}, status=403)

    article = get_object_or_404(Article, id=pk)
    article.approved = True
    article.save()

    send_mail(
        subject="Article Approved",
        message=f"{article.title} approved",
        from_email="noreply@news.com",
        recipient_list=["test@example.com"],
        fail_silently=True,
    )

    try:
        requests.post(
            "http://localhost:8000/api/approved/",
            json={"article_id": article.id, "title": article.title}
        )
    except:
        pass

    return Response({"message": "Approved"}, status=200)


# =========================
# APPROVED LOG
# =========================
@api_view(['POST'])
def approved_log(request):
    return Response({"message": "Received", "data": request.data})


# =========================
# NEWSLETTERS
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def newsletters(request):
    data = Newsletter.objects.all()
    return Response(NewsletterSerializer(data, many=True).data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_newsletter(request):

    if not request.user.groups.filter(name__in=["Journalist", "Editor"]).exists():
        return Response({"error": "Not allowed"}, status=403)

    serializer = NewsletterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_newsletter(request, pk):

    newsletter = get_object_or_404(Newsletter, id=pk)

    if not request.user.groups.filter(name__in=["Journalist", "Editor"]).exists():
        return Response({"error": "Not allowed"}, status=403)

    serializer = NewsletterSerializer(newsletter, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_newsletter(request, pk):

    newsletter = get_object_or_404(Newsletter, id=pk)

    if not request.user.groups.filter(name__in=["Journalist", "Editor"]).exists():
        return Response({"error": "Not allowed"}, status=403)

    newsletter.delete()
    return Response({"message": "Deleted"}, status=204)
