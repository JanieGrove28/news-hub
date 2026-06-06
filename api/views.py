"""
API Views for the News application.

Provides RESTful endpoints for:
- Articles (CRUD, approval, filtering)
- Newsletters (CRUD)
- Approved article notifications
- Subscription-based article retrieval

All endpoints use Django REST Framework.
"""

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
    """
    Returns all articles that have been approved by an editor.

    Public endpoint for retrieving published content.
    """
    articles = Article.objects.filter(approved=True)
    return Response(ArticleSerializer(articles, many=True).data)


# =========================
# SUBSCRIBED ARTICLES
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subscribed_articles(request):
    """
    Returns articles based on the user's subscriptions.

    Includes:
    - Articles from subscribed journalists
    - Articles from subscribed publishers
    """
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
    """
    Retrieves a single article by its ID.
    """
    article = get_object_or_404(Article, id=pk)
    return Response(ArticleSerializer(article).data)


# =========================
# CREATE ARTICLE (API)
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article_api(request):
    """
    Allows journalists to create new articles via API.

    The logged-in user is set as the article author.
    """

    if not request.user.groups.filter(name="Journalist").exists():
        return Response({"error": "Only journalists allowed"}, status=403)

    serializer = ArticleSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


# =========================
# UPDATE ARTICLE (API)
# =========================
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_article(request, pk):
    """
    Allows journalists and editors to update an existing article.
    """

    article = get_object_or_404(Article, id=pk)

    if not request.user.groups.filter(name__in=["Journalist", "Editor"]).exists():
        return Response({"error": "Not allowed"}, status=403)

    serializer = ArticleSerializer(article, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# =========================
# DELETE ARTICLE (API)
# =========================
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_article(request, pk):
    """
    Allows journalists and editors to delete an article via API.
    """

    article = get_object_or_404(Article, id=pk)

    if not request.user.groups.filter(name__in=["Journalist", "Editor"]).exists():
        return Response({"error": "Not allowed"}, status=403)

    article.delete()
    return Response({"message": "Deleted"}, status=204)


# =========================
# APPROVE ARTICLE
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def approve_article(request, pk):
    """
    Allows editors to approve an article.

    Once approved:
    - Email notification is sent
    - External API endpoint is triggered
    """

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
    """
    Receives log data for approved articles.

    Simulates external system integration.
    """
    return Response({"message": "Received", "data": request.data})


# =========================
# NEWSLETTERS (API LIST)
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def newsletters(request):
    """
    Returns all newsletters in the system.

    Accessible only to authenticated users.
    """
    data = Newsletter.objects.all()
    return Response(NewsletterSerializer(data, many=True).data)


# =========================
# CREATE NEWSLETTER (API)
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_newsletter(request):
    """
    Allows journalists and editors to create newsletters via API.

    The logged-in user is set as the author.
    """

    if not request.user.groups.filter(name__in=["Journalist", "Editor"]).exists():
        return Response({"error": "Not allowed"}, status=403)

    serializer = NewsletterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


# =========================
# UPDATE NEWSLETTER
# =========================
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_newsletter(request, pk):
    """
    Allows journalists and editors to update a newsletter.
    """

    newsletter = get_object_or_404(Newsletter, id=pk)

    if not request.user.groups.filter(name__in=["Journalist", "Editor"]).exists():
        return Response({"error": "Not allowed"}, status=403)

    serializer = NewsletterSerializer(newsletter, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# =========================
# DELETE NEWSLETTER
# =========================
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_newsletter(request, pk):
    """
    Allows journalists and editors to delete newsletters via API.
    """

    newsletter = get_object_or_404(Newsletter, id=pk)

    if not request.user.groups.filter(name__in=["Journalist", "Editor"]).exists():
        return Response({"error": "Not allowed"}, status=403)

    newsletter.delete()
    return Response({"message": "Deleted"}, status=204)