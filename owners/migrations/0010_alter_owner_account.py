# Generated by Django 4.2.3 on 2023-07-31 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('owners', '0009_remove_owner_pet_owner_neutering_owner_pet_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners', to=settings.AUTH_USER_MODEL),
        ),
    ]
