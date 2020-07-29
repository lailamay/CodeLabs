from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        User = get_user_model()
        model = User
        fields = ["username", "email", "password1", "password2"]

