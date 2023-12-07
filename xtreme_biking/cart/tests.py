from django.test import TestCase

class Item:
    pass

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)

class CartTests(TestCase):
    def test_cart_creation(self):
        cart = Cart()
        self.assertIsInstance(cart, Cart)

class CartTestCase(TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_add_item_to_cart(self):
        item = Item()
        self.cart.add_item(item)
        self.assertEqual(len(self.cart.items), 1)

    def test_remove_item_from_cart(self):
        item = Item()
        self.cart.add_item(item)
        self.cart.remove_item(item)
        self.assertEqual(len(self.cart.items), 0)
