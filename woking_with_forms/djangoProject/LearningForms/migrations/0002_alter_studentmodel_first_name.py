# Generated by Django 5.0.2 on 2024-02-08 12:09

import djangoProject.LearningForms.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningForms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='first_name',
            field=models.CharField(max_length=35, validators=[djangoProject.LearningForms.validators.validate_non_white_space]),
        ),
    ]
