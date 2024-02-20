from django.core.exceptions import ValidationError


def validate_non_white_space(value):
    if " " in value:
        raise ValidationError(message='This field has white space')