<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm

def register(request):
    """
    Handles user registration and assigns them to a group based on role.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            role = form.cleaned_data.get('role')

            group, created = Group.objects.get_or_create(name=role)
            user.groups.add(group)

            return redirect('login')

    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> bf8953c5044d80824794e9511acb31e28f75b7b6
