from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Form for registering new users with role selection.
    """

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")

        return email
