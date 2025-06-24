from django.contrib import admin
from .models import (
    Assistant,
    Breed,
    Category,
    File,
    Knowledges,
    Medrecord,
    Pets,
    Petsprofile,
    Product,
    Role,
    Shop,
    Shopproduct,
    Species,
    UserProfile,
    Userassistant,
    Userknowledges,
    Users,
)

admin.site.register(Assistant)
admin.site.register(Breed)
admin.site.register(Category)
admin.site.register(File)
admin.site.register(Knowledges)
admin.site.register(Medrecord)
admin.site.register(Pets)
admin.site.register(Petsprofile)
admin.site.register(Product)
admin.site.register(Role)
admin.site.register(Shop)
admin.site.register(Species)
admin.site.register(UserProfile)
admin.site.register(Users)
