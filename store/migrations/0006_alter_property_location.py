# Generated by Django 4.1.4 on 2023-01-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_location_alter_property_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=1000),
        ),
    ]