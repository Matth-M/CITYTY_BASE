# Generated by Django 4.2.3 on 2023-10-22 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0003_compte_attente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compte_attente',
            name='email',
            field=models.EmailField(max_length=150, unique=True),
        ),
    ]
