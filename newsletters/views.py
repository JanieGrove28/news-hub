"""
Views for the Newsletters app.

Handles listing, creating, editing, and deleting newsletters.
Each newsletter is a curated collection of articles created by journalists or editors.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Newsletter
from .forms import NewsletterForm


# =========================
# NEWSLETTER LIST
# =========================
@login_required
def newsletter_list(request):
    """
    Displays a list of all newsletters.

    Users can view all available newsletters in the system.
    """
    newsletters = Newsletter.objects.all()
    return render(request, "newsletters/newsletter_list.html", {
        "newsletters": newsletters
    })


# =========================
# CREATE NEWSLETTER
# =========================
@login_required
def create_newsletter(request):
    """
    Allows journalists and editors to create a new newsletter.

    The logged-in user is automatically assigned as the author.
    The newsletter can include multiple selected articles.
    """

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


# =========================
# EDIT NEWSLETTER
# =========================
@login_required
def edit_newsletter(request, pk):
    """
    Allows the author or an editor to edit an existing newsletter.

    Users can update title, description, and included articles.
    """

    newsletter = get_object_or_404(Newsletter, id=pk)

    form = NewsletterForm(request.POST or None, instance=newsletter)

    if form.is_valid():
        form.save()
        return redirect("newsletter_list")

    return render(request, "newsletters/newsletter_form.html", {
        "form": form
    })


# =========================
# DELETE NEWSLETTER
# =========================
@login_required
def delete_newsletter(request, pk):
    """
    Allows the author or an editor to delete a newsletter.

    Requires confirmation before permanent deletion.
    """

    newsletter = get_object_or_404(Newsletter, id=pk)

    if request.method == "POST":
        newsletter.delete()
        return redirect("newsletter_list")

    return render(request, "newsletters/newsletter_confirm_delete.html", {
        "newsletter": newsletter
    })
