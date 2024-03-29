# Generated by Django 4.1.4 on 2023-01-18 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_property_options_remove_property_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('instituition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='store.instituition')),
            ],
        ),
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='store.location'),
        ),
    ]
