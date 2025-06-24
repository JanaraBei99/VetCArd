# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Assistant(models.Model):
    assistant_id = models.AutoField(primary_key=True)
    assistant_sms = models.TextField()

    class Meta:
        managed = False
        db_table = 'assistant'

class Breed(models.Model):
    breed_id = models.AutoField(primary_key=True)
    breed_name = models.CharField(max_length=50)
    species = models.ForeignKey('Species', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'breed'


class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    url = models.TextField()
    size = models.IntegerField(blank=True, null=True)
    uploadedat = models.DateTimeField(blank=True, null=True)
    record = models.ForeignKey('Medrecord', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'file'


class Knowledges(models.Model):
    knowledges_id = models.AutoField(primary_key=True)
    knowledges = models.TextField()

    class Meta:
        managed = False
        db_table = 'knowledges'


class Medrecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    pet = models.ForeignKey('Pets', models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    clinicorvet = models.CharField(max_length=50, blank=True, null=True)
    dosage = models.CharField(max_length=30, blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medrecord'


class Pets(models.Model):
    pet_id = models.AutoField(primary_key=True)
    pets_name = models.CharField(max_length=50)
    species = models.ForeignKey('Species', models.DO_NOTHING)
    birthdate = models.DateField(blank=True, null=True)
    imageurl = models.CharField(max_length=255, blank=True, null=True)
    specialnotes = models.TextField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pets'


class Petsprofile(models.Model):
    animals_id = models.AutoField(primary_key=True)
    breed = models.ForeignKey(Breed, models.DO_NOTHING)
    breedcharacteristics = models.TextField(blank=True, null=True)
    commonname = models.CharField(max_length=50, blank=True, null=True)
    scientificname = models.CharField(max_length=50, blank=True, null=True)
    taxonomyclass = models.CharField(max_length=50, blank=True, null=True)
    conservationstatus = models.CharField(max_length=50, blank=True, null=True)
    habitat = models.CharField(max_length=50, blank=True, null=True)
    diet = models.CharField(max_length=50, blank=True, null=True)
    averagelifespan = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    colour = models.CharField(max_length=10, blank=True, null=True)
    behavior = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'petsprofile'

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'category'

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    imageurl = models.BinaryField(blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product'


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.role_name

    class Meta:
        managed = False
        db_table = 'role'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'



class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shop'


class Shopproduct(models.Model):
    pk = models.CompositePrimaryKey('shop_id', 'product_id')
    shop = models.ForeignKey(Shop, models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shopproduct'


class Species(models.Model):
    species_id = models.AutoField(primary_key=True)
    species_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'species'


class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, models.DO_NOTHING)
    fullname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    preferredlanguage = models.CharField(max_length=20, blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'user_profile'


class Userassistant(models.Model):
    pk = models.CompositePrimaryKey('user_id', 'assistant_id')
    user = models.ForeignKey('Users', models.DO_NOTHING)
    assistant = models.ForeignKey(Assistant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'userassistant'


class Userknowledges(models.Model):
    pk = models.CompositePrimaryKey('user_id', 'knowledges_id')
    user = models.ForeignKey('Users', models.DO_NOTHING)
    knowledges = models.ForeignKey(Knowledges, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'userknowledges'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(Role, models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users'
