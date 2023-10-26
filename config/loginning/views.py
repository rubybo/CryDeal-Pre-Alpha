from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, View
from django.urls import reverse_lazy

from .forms import *


# # Cbv LoginView
# class LoginUser(LoginView):
#     form_class = UserLoginForm
#     template_name = 'loginning/login.html'
#
#
# # Cbv LogoutView
# class LogoutUser(LogoutView):
#     template_name = 'core/base.html'
#
#     def get_success_url(self):
#         return reverse_lazy('loginning:user-login')

class RegisterView(CreateView):
    form_class = SignupForm
    template_name = 'loginning/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = SigninForm
    template_name = 'loginning/auth.html'


class LogoutUser(LogoutView):
    next_page = '/'
