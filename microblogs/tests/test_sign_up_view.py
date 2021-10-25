"""Tests of the sign up view!"""
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.test import TestCase
from microblogs.forms import SignUpForm
from microblogs.models import User
from .helper import LogInTester


class SignUpViewTestCase(TestCase, LogInTester):

    def setUp(self):
        self.url = reverse('sign_up')
        self.form_input = {
            'first_name': 'Musab',
            'last_name': 'Khan',
            'username': '@Mkhan',
            'email': 'mk@example.com',
            'bio': 'my bio',
            'password': 'Password123',
            'password_confirmation': 'Password123'
        }

    def test_sign_up_url(self):
        self.assertEqual(self.url,'/sign_up/')

    def test_get_sign_up(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertFalse(form.is_bound)



    def test_unsuccesful_sign_up(self):
        self.form_input['username'] = 'BADUSERNAME'
        response = self.client.post(self.url, self.form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertTrue(form.is_bound)
        self.assertFalse(self._is_logged_in())

    def test_successful_sign_up_view(self):
        response = self.client.post(self.url, self.form_input, follow=True)
        response_url = reverse('feed')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed((response, 'feed.html'))
        self.assertTrue(self._is_logged_in())




