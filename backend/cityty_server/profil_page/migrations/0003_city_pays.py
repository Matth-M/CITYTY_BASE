# Generated by Django 4.2.3 on 2023-10-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil_page', '0002_alter_city_adresse'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='pays',
            field=models.CharField(default='FRANCE', max_length=30),
        ),
    ]
