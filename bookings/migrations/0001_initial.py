# Generated by Django 4.2.3 on 2023-07-10 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boarders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kind', models.CharField(choices=[('boarder', 'Boarder'), ('sitter', 'Sitter')], max_length=15)),
                ('daycare_day', models.DateField(blank=True, null=True)),
                ('check_in', models.DateField(blank=True, null=True)),
                ('check_out', models.DateField(blank=True, null=True)),
                ('pets', models.PositiveIntegerField(default=1)),
                ('boarder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='boarders.boarder')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
