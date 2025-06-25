from django.contrib import admin

from .models import Role, Category


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_kg')
    search_fields = ('name_ru', 'name_kg',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_kg')
    search_fields = ('name_ru', 'name_kg',)
