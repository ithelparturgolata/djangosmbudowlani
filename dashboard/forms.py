from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput, FileInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(), label="Użytkownik")
    password = forms.CharField(widget=PasswordInput(), label="Hasło")

