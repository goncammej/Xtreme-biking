from django.test import TestCase
from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(title="Bike", price=1000, availability=5)
        Product.objects.create(title="Helmet", price=50, availability=10)

    def test_product_name(self):
        bike = Product.objects.get(title="Bike")
        helmet = Product.objects.get(title="Helmet")
        self.assertEqual(bike.title, "Bike")
        self.assertEqual(helmet.title, "Helmet")

    def test_product_price(self):
        bike = Product.objects.get(title="Bike")
        helmet = Product.objects.get(title="Helmet")
        self.assertEqual(bike.price, 1000)
        self.assertEqual(helmet.price, 50)

    def test_product_quantity(self):
        bike = Product.objects.get(title="Bike")
        helmet = Product.objects.get(title="Helmet")
        self.assertEqual(bike.availability, 5)
        self.assertEqual(helmet.availability, 10)
