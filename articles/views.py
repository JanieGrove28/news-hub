from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Article


def home(request):
    return render(request, 'articles/home.html')


@login_required
def create_article(request):

    if request.user.role != "journalist":
        return render(request, "articles/no_permission.html")

    if request.method == "POST":
        Article.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            author=request.user
        )
        return redirect('home')

    return render(request, 'articles/create_article.html')


@login_required
def approve_article(request, pk):

    if request.user.role != "editor":
        return render(request, "articles/no_permission.html")

    article = get_object_or_404(Article, id=pk)
    article.approved = True
    article.save()

    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')
