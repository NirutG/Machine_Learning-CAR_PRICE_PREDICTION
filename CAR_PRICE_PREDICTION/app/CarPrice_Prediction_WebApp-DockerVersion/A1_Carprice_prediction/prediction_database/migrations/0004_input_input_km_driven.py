# Generated by Django 4.2.4 on 2023-08-30 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction_database', '0003_remove_input_input_km_driven_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='input_km_driven',
            field=models.IntegerField(default='1', null=True),
        ),
    ]
