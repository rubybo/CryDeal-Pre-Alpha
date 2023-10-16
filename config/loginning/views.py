from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, reverse_lazy
from .forms import UserLoginForm


# Cbv LoginView
class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'loginning/login.html'


# Cbv LogoutView
class LogoutUser(LogoutView):
    template_name = 'core/base.html'

    def get_success_url(self):
        return reverse_lazy('loginning:user-login')
