from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        help_text=""
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput,
        help_text=""
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {
            "username": "",
        }
