from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article


@receiver(post_save, sender=Article)
def article_approved(sender, instance, **kwargs):
    if instance.approved:
        print(f"Article approved: {instance.title}")
