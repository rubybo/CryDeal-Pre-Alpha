from django.urls import path
from .views import LoginUser, LogoutUser

app_name = 'loginning'

urlpatterns = [
    path('user-login/', LoginUser.as_view(), name='user-login'),
    path('user-logout/', LogoutUser.as_view(), name='user-logout'),

]