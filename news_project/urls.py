from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from articles.views import home, create_article, approve_article

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('create/', create_article, name='create_article'),
    path('approve/<int:pk>/', approve_article, name='approve_article'),

    path('api/', include('api.urls')),
]
