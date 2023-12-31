# Generated by Django 4.2.3 on 2023-07-28 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('petname', models.CharField(max_length=80)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('breed', models.CharField(max_length=80)),
                ('neutering', models.BooleanField()),
                ('description', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
