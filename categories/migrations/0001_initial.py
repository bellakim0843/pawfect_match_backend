# Generated by Django 4.2.3 on 2023-07-21 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=80)),
                ('category_kind', models.CharField(choices=[('daycare', 'Daycare'), ('boading', 'Boarding')], max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
