from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import CustomUser
from accounts import views
from django.contrib import auth
from django.db import transaction


class AccountsTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            name='Test User',
            email='testemail@test.com',
            password='testpassword'
        )

    def test_login(self):
        response = self.client.post(
            reverse('accounts:login'), {'email': self.user.email, 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(email=self.user.email, password='testpassword')
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')  # Verifica que la respuesta es una redirección a la página de inicio de sesión

    def test_profile(self):
        self.client.login(email=self.user.email, password='testpassword')
        response = self.client.get(reverse('client_dashboard'))
        self.assertEqual(response.status_code, 200)
        

    def test_register(self):
        response = self.client.post(reverse('accounts:signup'), {
            'name': 'Test User 2',
            'email': 'useremail@example.com',
            'password1': 'testpassword1'
        })
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        response = self.client.post(
            reverse('accounts:login'), {'email': 'invalidemail', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)