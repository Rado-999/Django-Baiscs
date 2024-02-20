from django import forms

from djangoProject.LearningForms.models import StudentModel


class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=35,
        required=True,
    )

    last_name = forms.CharField(
        max_length=35,
        required=True,
    )

    age = forms.IntegerField(
        required=True
    )

    description = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Tell about yourself',
                'rows': 5,
                'cols': 50
            }
        )
    )

    sports = forms.CharField(
        widget=forms.RadioSelect(
            choices=(
                (1, 'football'),
                (2, 'basketball'),
                (3, 'box')
            )
        )
    )

    INTERESTS = (
        (1, 'Gaming'),
        (2, 'Reading'),
        (3, 'Drawing'),
        (4, 'Watching'),
        (5, 'Drafting'),

    )

    interest = forms.IntegerField(
        widget=forms.Select(choices=INTERESTS)
    )

    MUSICS = (
        (1, 'Pop'),
        (2, 'Pop-folk'),
        (3, 'Metal'),
        (4, 'Rap')
    )

    music = forms.ChoiceField(
        choices=MUSICS
    )


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        exclude = ['music']
