# Generated by Django 4.2.3 on 2023-07-28 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_pet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='updated_at',
        ),
    ]
