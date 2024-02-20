from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_white_space(value):
    if " " in value:
        raise ValidationError("White space in not allowed in name")


class ModelOne(models.Model):
    MIN_LENGTH_FIRST_NAME = 3
    MIN_LENGTH_LAST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 10
    MAX_LENGTH_LAST_NAME = 10

    name = models.CharField(
        max_length= MAX_LENGTH_FIRST_NAME,
        validators=[validate_white_space,
                    MinLengthValidator(MIN_LENGTH_FIRST_NAME)],
        null = False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=[validate_white_space,
                    MinLengthValidator(MIN_LENGTH_LAST_NAME)],
    )
    age = models.IntegerField()
    email = models.EmailField()
    profile_pic = models.ImageField(
        upload_to='web/profile_pics',
        null = True,
        blank = True
    )

    def save(self, *args, **kwargs):
        if self.age:
            self.age += 5
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    job = models.CharField(max_length=100)
    profile_pic = models.ImageField(
        upload_to='web/profile_pics',
        null= True,
        blank=True
    )