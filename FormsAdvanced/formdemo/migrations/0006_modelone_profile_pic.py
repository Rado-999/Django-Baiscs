# Generated by Django 4.2.10 on 2024-02-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formdemo', '0005_person_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelone',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='web/profile_pics'),
        ),
    ]