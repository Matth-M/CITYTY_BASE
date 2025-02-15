# Generated by Django 4.2.3 on 2023-10-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0005_delete_compte'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('name', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=30)),
                ('code_postal', models.CharField(max_length=10)),
                ('adresse', models.CharField(max_length=50)),
            ],
        ),
    ]
