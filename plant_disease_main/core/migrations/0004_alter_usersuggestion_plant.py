# Generated by Django 5.0.1 on 2024-01-16 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_diesease_image_plant_disease_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersuggestion',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userplant'),
        ),
    ]
