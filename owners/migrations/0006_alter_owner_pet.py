# Generated by Django 4.2.3 on 2023-07-31 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0005_alter_owner_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='pet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owners_pet', to='owners.pet'),
        ),
    ]