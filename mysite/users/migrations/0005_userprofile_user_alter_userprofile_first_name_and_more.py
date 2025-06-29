# Generated by Django 5.2.3 on 2025-06-25 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userprofile_options_alter_users_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.users'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='surname',
            field=models.CharField(max_length=50),
        ),
    ]
