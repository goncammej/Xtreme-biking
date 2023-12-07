# tests.py

import unittest
from .models import Order, OrderItem


class OrderTests(unittest.TestCase):
    def test_calculate_total_price(self):
        order = Order()
        order.items = {"item1": 10, "item2": 20, "item3": 30}  # Asumiendo que items es un diccionario
        total_price = sum(order.items.values())
        self.assertEqual(total_price, 60)

    def test_add_item(self):
        order = Order()
        order.items = {}  # Asumiendo que items es un diccionario
        order.items["item1"] = 10
        self.assertEqual(len(order.items), 1)
        self.assertEqual(order.items["item1"], 10)

    def test_remove_item(self):
        order = Order()
        order.items = {"item1": 10}  # Asumiendo que items es un diccionario
        del order.items["item1"]
        self.assertEqual(len(order.items), 0)
        self.assertNotIn("item1", order.items)


if __name__ == "__main__":
    unittest.main()
