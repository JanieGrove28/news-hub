from rest_framework import serializers
from articles.models import Article
from users.models import CustomUser
from newsletters.models import Newsletter


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for Article model.

    Converts Article instances to JSON format and validates incoming API data.
    """

    class Meta:
        model = Article
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model.

    Used to expose user data through the API in a structured format.
    """

    class Meta:
        model = CustomUser
        fields = '__all__'


class NewsletterSerializer(serializers.ModelSerializer):
    """
    Serializer for Newsletter model.

    Converts Newsletter instances to JSON format including related articles.
    """

    class Meta:
        model = Newsletter
        fields = '__all__'