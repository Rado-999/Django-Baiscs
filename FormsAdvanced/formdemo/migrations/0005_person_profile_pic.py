# Generated by Django 4.2.10 on 2024-02-20 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formdemo', '0004_person_alter_modelone_last_name_alter_modelone_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='web/profile_pics'),
        ),
    ]
