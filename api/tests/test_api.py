from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase
from rest_framework import status

from articles.models import Article
from newsletters.models import Newsletter


# =========================
# BASE SETUP
# =========================
class APITestSetup(APITestCase):

    def setUp(self):
        # Groups
        self.reader_group = Group.objects.create(name="Reader")
        self.journalist_group = Group.objects.create(name="Journalist")
        self.editor_group = Group.objects.create(name="Editor")

        # Users
        self.reader = User.objects.create_user(username="reader", password="pass123")
        self.journalist = User.objects.create_user(username="journalist", password="pass123")
        self.editor = User.objects.create_user(username="editor", password="pass123")

        self.reader.groups.add(self.reader_group)
        self.journalist.groups.add(self.journalist_group)
        self.editor.groups.add(self.editor_group)

        # Article
        self.article = Article.objects.create(
            title="Test Article",
            content="Test content",
            author=self.journalist,
            approved=True
        )

        # Newsletter
        self.newsletter = Newsletter.objects.create(
            title="Test Newsletter",
            description="Desc",
            author=self.journalist
        )


# =========================
# AUTH TESTS
# =========================
class AuthenticationTests(APITestSetup):

    def test_login_required_for_subscribed_articles(self):
        response = self.client.get("/api/articles/subscribed/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# =========================
# ARTICLE TESTS
# =========================
class ArticleTests(APITestSetup):

    def test_get_approved_articles(self):
        response = self.client.get("/api/articles/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_article(self):
        response = self.client.get(f"/api/articles/{self.article.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_journalist_can_create_article(self):
        self.client.login(username="journalist", password="pass123")

        data = {
            "title": "New Article",
            "content": "Content"
        }

        response = self.client.post("/api/articles/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_reader_cannot_create_article(self):
        self.client.login(username="reader", password="pass123")

        data = {
            "title": "Fail Article",
            "content": "Content"
        }

        response = self.client.post("/api/articles/create/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# =========================
# PERMISSION TESTS
# =========================
class PermissionTests(APITestSetup):

    def test_editor_can_delete_article(self):
        self.client.login(username="editor", password="pass123")

        response = self.client.delete(f"/api/articles/{self.article.id}/delete/")
        self.assertIn(response.status_code, [200, 204])

    def test_reader_cannot_delete_article(self):
        self.client.login(username="reader", password="pass123")

        response = self.client.delete(f"/api/articles/{self.article.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# =========================
# NEWSLETTER TESTS
# =========================
class NewsletterTests(APITestSetup):

    def test_get_newsletters(self):
        response = self.client.get("/api/newsletters/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_journalist_can_create_newsletter(self):
        self.client.login(username="journalist", password="pass123")

        data = {
            "title": "New Newsletter",
            "description": "Desc"
        }

        response = self.client.post("/api/newsletters/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_reader_cannot_create_newsletter(self):
        self.client.login(username="reader", password="pass123")

        data = {
            "title": "Fail Newsletter",
            "description": "Desc"
        }

        response = self.client.post("/api/newsletters/create/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# =========================
# SUBSCRIPTION TESTS
# =========================
class SubscriptionTests(APITestSetup):

    def test_subscribed_articles_requires_auth(self):
        response = self.client.get("/api/articles/subscribed/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# =========================
# APPROVAL LOGIC PLACEHOLDER TEST
# =========================
class ApprovalTests(APITestSetup):

    def test_article_is_approved_flag(self):
        self.assertTrue(self.article.approved)
