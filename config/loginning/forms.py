from django import forms
from django.contrib.auth.forms import AuthenticationForm


# Redefining the standard Authentication form
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput,
        label='Имя пользователя')
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(),
    )
