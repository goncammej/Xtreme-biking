from django.test import TestCase
from django.contrib.auth.models import User
from accounts.urls import reverse
from .models import CustomUser


class AccountsTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            name='Test User',
            email='testemail@test.com',
            password='testpassword'
        )

    def test_login(self):
        response = self.client.post(
            reverse('login'), {'email': self.user.email, 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Logged in successfully')

    def test_logout(self):
        self.client.login(email=self.user.email, password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Logged out successfully')

    def test_profile(self):
        self.client.login(name=self.user.name, password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to your profile')

    def test_register(self):
        response = self.client.post(
            reverse('signup'), {'name': 'newuser', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Registration successful')

    def test_invalid_login(self):
        response = self.client.post(
            reverse('login'), {'name': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')
