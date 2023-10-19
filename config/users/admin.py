from django.contrib import admin
from django.contrib.auth.models import User
from django.core.paginator import Paginator


class NoCountPaginator(Paginator):
    @property
    def count(self):
        return 9999999


# Fine-tuning the User model for the admin panel
class Users(admin.ModelAdmin):
    search_fields = ['username']
    paginator = NoCountPaginator


# Unregistering the default model
admin.site.unregister(User)
admin.site.register(User, Users)
