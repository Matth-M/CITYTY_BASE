# Generated by Django 4.2.3 on 2023-11-12 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_abonnement_surname_abonnement_ville'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonnement',
            name='vue',
            field=models.BooleanField(default=False),
        ),
    ]
