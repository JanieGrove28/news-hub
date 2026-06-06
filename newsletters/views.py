from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Newsletter
from .forms import NewsletterForm


@login_required
def newsletter_list(request):
    newsletters = Newsletter.objects.all()
    return render(request, "newsletters/newsletter_list.html", {
        "newsletters": newsletters
    })


@login_required
def create_newsletter(request):

    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.author = request.user
            newsletter.save()
            form.save_m2m()
            return redirect("newsletter_list")

    else:
        form = NewsletterForm()

    return render(request, "newsletters/newsletter_form.html", {
        "form": form
    })


@login_required
def edit_newsletter(request, pk):
    newsletter = get_object_or_404(Newsletter, id=pk)

    form = NewsletterForm(request.POST or None, instance=newsletter)

    if form.is_valid():
        form.save()
        return redirect("newsletter_list")

    return render(request, "newsletters/newsletter_form.html", {
        "form": form
    })


@login_required
def delete_newsletter(request, pk):
    newsletter = get_object_or_404(Newsletter, id=pk)

    if request.method == "POST":
        newsletter.delete()
        return redirect("newsletter_list")

    return render(request, "newsletters/newsletter_confirm_delete.html", {
        "newsletter": newsletter
    })
