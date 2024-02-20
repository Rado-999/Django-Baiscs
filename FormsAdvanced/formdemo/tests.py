from django.core.exceptions import ValidationError
from django.test import TestCase

from FormsAdvanced.formdemo import models
from FormsAdvanced.formdemo.models import ModelOne

valid_instance= ModelOne(name="test",last_name='tested', age=20,email='test01@gmail.com')
invalid_instance= ModelOne(name='test', last_name='tested', age=20, email='test01@gmail.com')

class MyFormTests(TestCase):
    def test_validator_success(self):
        valid_instance.full_clean()
        valid_instance.save()

    def test_validator_error(self):
        with self.assertRaises(ValidationError):
            invalid_instance.full_clean()