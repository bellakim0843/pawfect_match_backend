# Generated by Django 4.2.3 on 2023-07-21 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitters', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitter',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sitters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sitter',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sitters', to='categories.category'),
        ),
        migrations.AddField(
            model_name='sitter',
            name='services',
            field=models.ManyToManyField(related_name='sitters', to='sitters.service'),
        ),
    ]
