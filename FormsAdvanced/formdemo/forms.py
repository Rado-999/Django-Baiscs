from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelform_factory, modelformset_factory
from crispy_forms.helper import FormHelper
from FormsAdvanced.formdemo.models import ModelOne, Person


class ReadonlyFieldMixin:
    readonly_fields = []

    def _mark_readonly_fields(self):
        for field_name in self.readonly_fields:
            self.fields[field_name].widget.attrs["readonly"] = True

        # for _,field in self.fields.items():
        #     field.widget.attrs['readonly'] = True


class MyModelForm(forms.ModelForm):
    class Meta:
        model = ModelOne
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Enter your name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['age'].widget.attrs['placeholder'] = 'Enter your age'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter a valid email'

    def clean(self):
        cleaned_data = super().clean()
        self.clean_name()
        self.clean_last_name()
        self.clean_age()
        self.clean_email()
        self.validate_custom_condition()
        return cleaned_data

    # if cleaned_data['name'] == cleaned_data['last_name']:
    #     raise ValidationError('Cannot be simillar')
    #
    # return cleaned_data

    # self.clean_name()
    # self.clean_last_name()
    # self.clean_age()
    # self.clean_email()

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            if name[0] != 'R':
                raise ValidationError('Name must start with "R".')
            elif name[-1] != 'v':
                raise ValidationError('Name must end with "v".')

        return name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name:
            if len(last_name) != 8:
                raise ValidationError('Last name must be 8 characters.')

        return last_name

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and age < 20:
            raise ValidationError('Age must be at least 20')

        return age

    def clean_email(self):
        email = str(self.cleaned_data.get('email'))
        if '.com' not in email:
            raise ValidationError('Email must have ".com".')

        return email

    # def is_valid(self):
    #     # return super().is_valid()
    #
    #     valid = super().is_valid()
    #     self.validate_custom_condition()
    #     return valid

    def validate_custom_condition(self):
        # if not self.is_bound or not self.is_valid():
        #     return

        email = self.cleaned_data.get('email')
        if email:
            if 'gmail.bg' in email:
                raise ValidationError('Gmail address must not contain "bg". They must end with ".com".')
            elif 'abv.com' in email:
                raise ValidationError('Abv address must not contain "com". They must end with ".bg"')

        return email


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'




PersonFormSet = modelformset_factory(Person, form=PersonForm, extra=2)


class CrispyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'



class ModelForm2(ReadonlyFieldMixin, MyModelForm):
    readonly_fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._mark_readonly_fields()
        self.fields["age"].widget.attrs["readonly"] = "readonly"

    def clean(self):
        print(f'Clened data is called {super().clean()}')
        cleaned_data = super().clean()

        print('Before check')

        if cleaned_data['first_name'] == cleaned_data['last_name']:
            print(cleaned_data['first_name'])
            raise ValidationError('Incorrect names')

        print('After check')

        return cleaned_data


PersonForm2 = modelform_factory(ModelOne, fields=('__all__'))
