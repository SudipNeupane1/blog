import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.test import TestCase

class BogConfigTest(TestCase):
    def test_secret_key_strength(self):
        # self.assertNotEqual(1,2)
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        # self.assertNotEqual(SECRET_KEY,'abc')
       
        try:
            is_strong = validate_password(SECRET_KEY)
        except Execption as e:
            msg = f'Bad Secret Key{e.messages}'
            self.fail(msg)