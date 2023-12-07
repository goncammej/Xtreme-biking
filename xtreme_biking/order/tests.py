# tests.py

import unittest
from .models import Order


class OrderTests(unittest.TestCase):
    def add_item(self, order, item_name, quantity):
        order.items[item_name] = quantity

    def test_calculate_total_price(self):
        order = Order()
        order.add_item(order, "item1", 10)
        order.add_item(order, "item2", 20)
        order.add_item(order, "item3", 30)
        self.assertEqual(order.calculate_total_price(), 60)

    def test_add_item(self):
        order = Order()
        order.add_item(order, "item1", 10)
        self.assertEqual(len(order.items), 1)
        self.assertEqual(order.items["item1"], 10)

    def test_remove_item(self):
        order = Order()
        order.add_item(order, "item1", 10)
        order.remove_item("item1")
        self.assertEqual(len(order.items), 0)
        self.assertNotIn("item1", order.items)


if __name__ == "__main__":
    unittest.main()
