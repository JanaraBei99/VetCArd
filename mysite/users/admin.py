from django.contrib import admin
from .models import User, UserProfile


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'login', 'role')
    search_fields = ('login',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_id', 'first_name', 'last_name', 'surname', 'email')
    search_fields = ('first_name', 'last_name', 'email')
