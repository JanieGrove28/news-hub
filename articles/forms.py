from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    """
    Form for creating and updating articles.

    Handles validation for article fields including title, content,
    and optional publisher assignment.
    """

    class Meta:
        model = Article
        fields = ['title', 'content', 'publisher']