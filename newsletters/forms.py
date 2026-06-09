from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    """
    Form for creating and editing newsletters.

    Allows selection of multiple articles to be included in a newsletter.
    """

    class Meta:
        model = Newsletter
        fields = ["title", "description", "articles"]