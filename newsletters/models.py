from django.db import models
from django.conf import settings


class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    # REQUIRED BY ASSIGNMENT
    articles = models.ManyToManyField(
        'articles.Article',
        blank=True,
        related_name='newsletters'
    )

    def __str__(self):
        return self.title
