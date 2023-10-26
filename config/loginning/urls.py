from django.urls import path
from .views import LoginUser, LogoutUser, RegisterView



urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout'),


]