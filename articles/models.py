from django.db import models
from django.conf import settings


class Publisher(models.Model):
    """
    Represents a publisher entity in the News Hub system.

    Publishers can create and manage multiple articles. They act as content
    sources for journalist-submitted or publisher-submitted news.
    """

    name = models.CharField(max_length=200)

    def __str__(self):
        """Return the name of the publisher."""
        return self.name


class Article(models.Model):
    """
    Represents a news article in the system.

    Articles are created by journalists and may optionally be linked to a
    publisher. Each article requires approval by an editor before being
    publicly visible to readers.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        """Return the title of the article."""
        return self.title
