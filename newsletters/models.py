from django.db import models
from django.conf import settings


class Newsletter(models.Model):
    """
    Represents a curated collection of articles.

    Newsletters are created by journalists or editors and can contain
    multiple articles grouped together for distribution or publication.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    articles = models.ManyToManyField(
        'articles.Article',
        blank=True,
        related_name='newsletters'
    )

    def __str__(self):
        """Return the title of the newsletter."""
        return self.title