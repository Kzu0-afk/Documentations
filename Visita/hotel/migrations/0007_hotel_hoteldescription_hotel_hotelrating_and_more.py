# Generated by Django 5.1.3 on 2024-11-28 13:16

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_entity', '0001_initial'),
        ('hotel', '0006_remove_hotel_is_featured_alter_hotel_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotelDescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotelRating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_entity.adminentity'),
        ),
    ]
