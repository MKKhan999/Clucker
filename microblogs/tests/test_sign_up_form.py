from django.test import TestCase
from microblogs.forms import SignUpForm
from django import forms
from microblogs.models import User
class SignUpFormTestCase(TestCase):

    def setUp(self):
        self.form_input = {
            'first_name': 'Musab',
            'last_name': 'Khan',
            'username': '@Mkhan',
            'email': 'mk@example.com',
            'bio': 'my bio',
            'new_password': '123',
            'password_confirmation': '123'
        }


    def test_valid_sign_up_form(self):
        form = SignUpForm(data=self.form_input)
        self.assertTrue(form.is_valid)


    def test_form_has_valid_fields(self):
        form = SignUpForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('email', form.fields)
        email_field = form.fields['email']
        self.assertTrue(isinstance(email_field, forms.EmailField))
        self.assertIn('bio', form.fields)
        self.assertIn('username', form.fields)
        self.assertIn('password', form.fields)
        self.assertIn('password_confirmation', form.fields)
        password_field = form.fields['password']
        self.assertFalse(isinstance(password_field, forms.PasswordInput))

    def test_form_uses_model(self):
        self.form_input['username'] = 'badusername'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_have_capital_letter(self):
        self.form_input['password'] = 'badpassword'
        self.form_input['password_confirmation'] = 'badpassword'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def same_password_as_password_confirmation(self):
        self.form_input['password_confirmation'] = 'incorrectpassword'
        form = SignUpForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_new_password_and_password_confirmation_are_identical(self):
        self.form_input['password_confirmation'] = 'WrongPassword123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())









