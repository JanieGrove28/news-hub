from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Article

User = get_user_model()

class ArticleTest(TestCase):

    def test_create_article(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpass",
            role="journalist"
        )

        article = Article.objects.create(
            title="Test Article",
            content="Test Content",
            author=user
        )

        self.assertEqual(article.title, "Test Article")
        self.assertEqual(article.author.username, "testuser")
