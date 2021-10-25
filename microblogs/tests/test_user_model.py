from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import User
from django.db import models

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
        '@johndoe',
        first_name='John',
        last_name='Doe',
        email='johndoe@example.org',
        password='Password123',
        bio='The quick brown fox jumps over the lazy dog.'
        )

    def test_valid_user(self):
        self._assert_user_is_valid()

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')

    def test_username_should_be_valid(self):

        user = User.objects.create_user(
            '@Mkhan',
            first_name='Musab',
            last_name='Khan',
            email='example@msn.com',
            password='123',
            bio='Nice',
        )
        user.username = ''
        with self.assertRaises(ValidationError):
            user.full_clean()



# Create your tests here.
