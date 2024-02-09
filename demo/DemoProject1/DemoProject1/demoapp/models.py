from django.db import models


# Create your models here.

class DemoModel(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
    )

    job = models.CharField(
        max_length=30,
    )

    title = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        default='Mr'
    )
