from django.db import models

from djangoProject.LearningForms.validators import validate_non_white_space

INTERESTS=(
        (1,'Gaming'),
        (2,'Reading'),
        (3,'Drawing'),
        (4,'Watching'),
        (5,'Drafting'),

    )


class StudentModel(models.Model):
    first_name = models.CharField(
        max_length=35,
        null=False,
        blank=False,
        validators=(validate_non_white_space,)
    )

    last_name = models.CharField(
        max_length=35,
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False
    )


    description = models.TextField(
        max_length=200,
        null=False,
        blank=False,
    )

    sports = models.IntegerField(
        choices=(
            (1, 'football'),
            (2, 'basketball'),
            (3, 'box')
        )
    )

    interests = models.IntegerField(
        choices=INTERESTS
    )

    MUSICS = (
        (1, 'Pop'),
        (2, 'Pop-folk'),
        (3, 'Metal'),
        (4, 'Rap')
    )

    music = models.IntegerField(
        choices=MUSICS,
        null=False,
        blank=False
    )

    @property
    def full_name(self):
        result = f'{self.first_name} {self.last_name}'
        return result

