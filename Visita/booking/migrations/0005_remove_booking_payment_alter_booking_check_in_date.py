# Generated by Django 5.1.3 on 2024-11-27 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_check_in_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='payment',
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateField(default=datetime.date(2024, 11, 27)),
        ),
    ]