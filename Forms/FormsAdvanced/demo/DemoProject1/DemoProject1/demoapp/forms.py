from django.forms import ModelForm
from .models import DemoModel
from django import forms


class MyModelForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        required=True,
        label='Full Name'
    )

    age = forms.IntegerField(
        required=True,
    )

    job = forms.CharField(
        max_length=30,
        required=True,
    )

    title = forms.CharField(
        max_length=2,
        required=True,
        initial='M',
    )

    about_me = forms.CharField(
        widget=forms.Textarea,
        label='Description',
        initial='Tell about yourself'
    )

    sports = forms.ChoiceField(
        choices = (
            (1, 'Football'),
            (2, 'Basetball'),
            (3, 'Boxing'),
            (4, 'Others'),
        ),
        required=False
    )

