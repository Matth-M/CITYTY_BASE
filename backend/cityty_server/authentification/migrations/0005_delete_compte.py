# Generated by Django 4.2.3 on 2023-10-23 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0004_alter_compte_attente_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Compte',
        ),
    ]
