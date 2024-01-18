# Generated by Django 4.2.3 on 2023-11-12 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil_page', '0003_city_pays'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0008_delete_abonnement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonnements',
            name='lastMsg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chat.message'),
        ),
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('surname', models.CharField(blank=True, max_length=255, null=True)),
                ('ville', models.CharField(blank=True, max_length=255, null=True)),
                ('vue', models.BooleanField(default=False)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('LastMsg', models.TextField()),
                ('userLastMsg', models.CharField(max_length=255)),
                ('dateLastMsg', models.DateTimeField()),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil_page.city')),
                ('lastMsg', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chat.message')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
