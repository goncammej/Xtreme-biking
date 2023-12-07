from django.test import TestCase
from .models import Client


class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name="John Doe", email="johndoe@example.com")

    def test_client_creation(self):
        client = Client.objects.get(name="John Doe")
        self.assertEqual(client.email, "johndoe@example.com")
