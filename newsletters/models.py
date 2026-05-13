from django.db import models
from django.conf import settings
from articles.models import Article

<<<<<<< HEAD

class Publisher(models.Model):
    """
    Represents a news publisher that can have multiple editors and journalists.
    """
    name = models.CharField(max_length=255)

    editors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='publisher_editors',
        limit_choices_to={'role': 'Editor'},
        blank=True
    )

    journalists = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='publisher_journalists',
        limit_choices_to={'role': 'Journalist'},
        blank=True
    )

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    """
    Represents a newsletter created by a user and containing multiple articles.
    """
=======
class Newsletter(models.Model):
>>>>>>> bf8953c5044d80824794e9511acb31e28f75b7b6
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.title
