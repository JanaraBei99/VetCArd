from django.db import models


class Assistant(models.Model):
    assistant_sms = models.TextField()

    class Meta:
        db_table = 'assistant'


class Breed(models.Model):
    breed_name = models.CharField(max_length=50)
    species = models.ForeignKey('Species', models.CASCADE)

    class Meta:
        db_table = 'breed'


class File(models.Model):
    url = models.TextField()
    size = models.IntegerField(blank=True, null=True)
    uploaded_date = models.DateTimeField(blank=True, null=True)
    record = models.ForeignKey('MedRecord', models.CASCADE)

    class Meta:
        db_table = 'file'


class Knowledge(models.Model):
    knowledge = models.TextField()

    class Meta:
        db_table = 'knowledge'


class MedRecord(models.Model):
    pet = models.ForeignKey('Pets', models.CASCADE)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    clinic_or_vet = models.CharField(max_length=50, blank=True, null=True)
    dosage = models.CharField(max_length=30, blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'med_record'


class Pets(models.Model):
    pets_name = models.CharField(max_length=50)
    species = models.ForeignKey('Species', models.CASCADE)
    birthdate = models.DateField(blank=True, null=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    special_notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey('User', models.CASCADE)

    class Meta:
        db_table = 'pets'


class PetProfile(models.Model):
    breed = models.ForeignKey(Breed, models.CASCADE)
    breed_characteristics = models.TextField(blank=True, null=True)
    common_name = models.CharField(max_length=50, blank=True, null=True)
    scientific_name = models.CharField(max_length=50, blank=True, null=True)
    taxonomy_class = models.CharField(max_length=50, blank=True, null=True)
    conservation_status = models.CharField(max_length=50, blank=True, null=True)
    habitat = models.CharField(max_length=50, blank=True, null=True)
    diet = models.CharField(max_length=50, blank=True, null=True)
    average_lifespan = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    colour = models.CharField(max_length=10, blank=True, null=True)
    behavior = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'pets_profile'


class Product(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey("reference.Category", models.CASCADE)

    class Meta:
        db_table = 'product'


class Shop(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey('User', models.CASCADE)

    class Meta:
        db_table = 'shop'


class ShopProduct(models.Model):
    shop = models.ForeignKey(Shop, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)

    class Meta:
        db_table = 'shop_product'


class Species(models.Model):
    species_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'species'


class UserAssistant(models.Model):
    user = models.ForeignKey('User', models.CASCADE)
    assistant = models.ForeignKey(Assistant, models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField('Users', on_delete=models.CASCADE, null=True)
    profile_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, models.DO_NOTHING)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    preferred_language = models.CharField(max_length=20, blank=True, null=True)
    clinic = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    specialization = models.CharField(max_length=50, blank=True, null=True)
    experience = models.CharField(max_length=50, blank=True, null=True)
    license_number = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    nameoforganization = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    class Meta:
        db_table = 'user_assistant'


class UserKnowledge(models.Model):
    user = models.ForeignKey('User', models.CASCADE)
    knowledge = models.ForeignKey(Knowledge, models.CASCADE)

    class Meta:
        db_table = 'user_knowledge'
