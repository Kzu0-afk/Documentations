# Generated by Django 5.1.3 on 2024-11-26 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_entity', '0002_hotel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='location',
            new_name='hotelName',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='price_per_night',
        ),
    ]
