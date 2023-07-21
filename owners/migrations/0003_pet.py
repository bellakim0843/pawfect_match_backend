# Generated by Django 4.2.3 on 2023-07-10 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('petname', models.CharField(max_length=80)),
                ('species', models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('etc', 'Etc')], max_length=20)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('breed', models.CharField(max_length=80)),
                ('neutering', models.BooleanField()),
                ('description', models.TextField(default='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='owners.owner')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
