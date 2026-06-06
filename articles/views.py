from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Article, Publisher


# =========================
# HOME (FIXED VISIBILITY)
# =========================
def home(request):
    articles = Article.objects.filter(approved=True)

    return render(
        request,
        'articles/home.html',
        {'articles': articles}
    )


# =========================
# CREATE ARTICLE
# =========================
@login_required
def create_article(request):

    if request.user.role != "journalist":
        return render(request, "articles/no_permission.html")

    publishers = Publisher.objects.all()

    if request.method == "POST":

        publisher_id = request.POST.get("publisher")
        publisher = None

        if publisher_id:
            publisher = Publisher.objects.get(id=publisher_id)

        Article.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            author=request.user,
            publisher=publisher,
            approved=False
        )

        return redirect('home')

    return render(
        request,
        'articles/create_article.html',
        {'publishers': publishers}
    )


# =========================
# ARTICLE DETAIL (NEW)
# =========================
@login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)

    return render(request, "articles/article_detail.html", {
        "article": article
    })


# =========================
# EDIT ARTICLE (NEW)
# =========================
@login_required
def edit_article(request, pk):

    article = get_object_or_404(Article, id=pk)

    if request.user != article.author and request.user.role not in ["editor"]:
        return render(request, "articles/no_permission.html")

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")

        publisher_id = request.POST.get("publisher")
        if publisher_id:
            article.publisher = Publisher.objects.get(id=publisher_id)

        article.save()
        return redirect("article_detail", pk=article.id)

    publishers = Publisher.objects.all()

    return render(request, "articles/edit_article.html", {
        "article": article,
        "publishers": publishers
    })


# =========================
# DELETE ARTICLE (NEW)
# =========================
@login_required
def delete_article(request, pk):

    article = get_object_or_404(Article, id=pk)

    if request.user != article.author and request.user.role != "editor":
        return render(request, "articles/no_permission.html")

    if request.method == "POST":
        article.delete()
        return redirect("home")

    return render(request, "articles/article_confirm_delete.html", {
        "article": article
    })


# =========================
# APPROVE ARTICLE
# =========================
@login_required
def approve_article(request, pk):

    if request.user.role != "editor":
        return render(request, "articles/no_permission.html")

    article = get_object_or_404(Article, id=pk)

    article.approved = True
    article.save()

    return redirect('home')


# =========================
# PUBLISHERS
# =========================
@login_required
def publisher_list(request):

    if request.user.role != "editor":
        return render(request, "articles/no_permission.html")

    if request.method == "POST":
        name = request.POST.get("name")

        if name:
            Publisher.objects.create(name=name)

        return redirect("publisher_list")

    publishers = Publisher.objects.all()

    return render(
        request,
        "articles/publisher_list.html",
        {"publishers": publishers}
    )


# =========================
# LOGOUT
# =========================
def logout_view(request):
    logout(request)
    return redirect('home')
