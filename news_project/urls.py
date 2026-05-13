from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
<<<<<<< HEAD

from articles.views import home, create_article, approve_article
from users.views import register 
=======
from articles.views import home, create_article, approve_article
>>>>>>> bf8953c5044d80824794e9511acb31e28f75b7b6

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

<<<<<<< HEAD
    # auth
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),  # ✅ ADD THIS

    # articles
    path('create/', create_article, name='create_article'),
    path('approve/<int:pk>/', approve_article, name='approve_article'),

    # api
=======
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('create/', create_article, name='create_article'),
    path('approve/<int:pk>/', approve_article, name='approve_article'),

>>>>>>> bf8953c5044d80824794e9511acb31e28f75b7b6
    path('api/', include('api.urls')),
]
