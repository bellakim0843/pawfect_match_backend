# Generated by Django 4.2.3 on 2023-07-30 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0010_booking_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]