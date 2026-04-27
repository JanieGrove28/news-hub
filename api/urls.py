from django.urls import path
from .views import (
    approved_articles,
    article_detail,
    create_article_api,
    update_article,
    delete_article,
    subscribed_articles
)

urlpatterns = [
    path('articles/', approved_articles),
    path('articles/<int:pk>/', article_detail),

    path('articles/create/', create_article_api),
    path('articles/update/<int:pk>/', update_article),
    path('articles/delete/<int:pk>/', delete_article),

    path('articles/subscribed/', subscribed_articles),
]
