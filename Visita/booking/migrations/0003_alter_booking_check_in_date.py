# Generated by Django 5.1.3 on 2024-11-25 03:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_bookingstatus_booking_booking_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateField(default=datetime.date(2024, 11, 25)),
        ),
    ]