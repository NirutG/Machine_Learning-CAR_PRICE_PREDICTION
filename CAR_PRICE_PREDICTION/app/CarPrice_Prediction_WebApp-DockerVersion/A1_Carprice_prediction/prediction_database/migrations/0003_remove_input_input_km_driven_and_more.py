# Generated by Django 4.2.4 on 2023-08-30 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prediction_database', '0002_output_remove_input_input_brand_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='input_km_driven',
        ),
        migrations.RemoveField(
            model_name='input',
            name='input_max_power',
        ),
    ]
