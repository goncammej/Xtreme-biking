from django.test import TestCase
from .models import Customer


class ClientTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="John Doe", email="johndoe@example.com")

    def test_client_creation(self):
        client = Customer.objects.get(name="John Doe")
        self.assertEqual(client.email, "johndoe@example.com")
