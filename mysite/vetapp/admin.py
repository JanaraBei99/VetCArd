from django.contrib import admin
from .models import (
    Assistant,
    Breed,
    File,
    Knowledge,
    MedRecord,
    Pets,
    PetProfile,
    Product,
    Shop,
    ShopProduct,
    Species,
    UserAssistant,
    UserKnowledge,
)

admin.site.register(Assistant)
admin.site.register(Breed)
admin.site.register(File)
admin.site.register(Knowledge)
admin.site.register(MedRecord)
admin.site.register(Pets)
admin.site.register(PetProfile)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(ShopProduct)
admin.site.register(Species)
admin.site.register(UserAssistant)
admin.site.register(UserKnowledge)
