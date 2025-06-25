from django.contrib import admin
from .models import Users, Role, UserProfile

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'login', 'role')
    search_fields = ('login',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_id', 'first_name', 'last_name', 'surname', 'email')
    search_fields = ('first_name', 'last_name', 'email')
