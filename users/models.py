from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model with roles and subscriptions.
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

    # Readers subscribe to journalists
    subscribed_journalists = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='journalist_subscribers',
        limit_choices_to={'role': 'journalist'}
    )