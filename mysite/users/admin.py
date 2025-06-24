from django.contrib import admin
from .models import Users  # или User, если ты используешь встроенную

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'role')  # замените на поля своей модели
    search_fields = ('login',)
