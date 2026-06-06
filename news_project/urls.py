from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from articles.views import (
    home,
    create_article,
    approve_article,
    publisher_list
)

from users.views import register


urlpatterns = [
    path('admin/', admin.site.urls),

    # home
    path('', home, name='home'),

    # auth
    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),

    # articles
    path('create/', create_article, name='create_article'),
    path('approve/<int:pk>/', approve_article, name='approve_article'),
    path('publishers/', publisher_list, name='publisher_list'),

    # api
    path('api/', include('api.urls')),

    # newsletters

    path('newsletters/', include('newsletters.urls')),

]
