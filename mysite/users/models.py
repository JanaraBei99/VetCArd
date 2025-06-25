from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    role = models.ForeignKey("reference.Role", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'


class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    preferred_language = models.CharField(max_length=20, blank=True, null=True)
    clinic = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    specialization = models.CharField(max_length=50, blank=True, null=True)
    experience = models.CharField(max_length=50, blank=True, null=True)
    license_number = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    name_of_organization = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'user_profile'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
