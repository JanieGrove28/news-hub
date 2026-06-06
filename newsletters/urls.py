from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter_list, name='newsletter_list'),
    path('create/', views.create_newsletter, name='create_newsletter'),
    path('edit/<int:pk>/', views.edit_newsletter, name='edit_newsletter'),
    path('delete/<int:pk>/', views.delete_newsletter, name='delete_newsletter'),
]