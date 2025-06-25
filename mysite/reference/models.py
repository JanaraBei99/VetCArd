from django.db import models


class BaseReference(models.Model):
    name_ru = models.CharField(max_length=100)
    name_kg = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        abstract = True


class Role(BaseReference):
    class Meta:
        db_table = 'role'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class Category(BaseReference):
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
