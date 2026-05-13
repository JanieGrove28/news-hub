from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model with roles and subscription preferences.
    """

    ROLE_CHOICES = (
        ('reader', 'Reader'),
        ('journalist', 'Journalist'),
        ('editor', 'Editor'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='reader'
    )

    subscribed_publishers = models.ManyToManyField(
        'newsletters.Publisher',
        blank=True,
        related_name='subscribers'
    )

    subscribed_journalists = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='journalist_subscribers',
        limit_choices_to={'role': 'journalist'}
    )
    