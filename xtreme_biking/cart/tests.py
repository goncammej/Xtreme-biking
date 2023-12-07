from django.test import TestCase
from .models import Cart, Item


class CartTestCase(TestCase):
    def setUp(self):
        self.cart = Cart.objects.create()

    def test_add_item_to_cart(self):
        item = Item.objects.create(name="Bike", price=1000)
        self.cart.add_item(item)
        self.assertEqual(self.cart.items.count(), 1)

    def test_remove_item_from_cart(self):
        item = Item.objects.create(name="Helmet", price=50)
        self.cart.add_item(item)
        self.cart.remove_item(item)
        self.assertEqual(self.cart.items.count(), 0)
