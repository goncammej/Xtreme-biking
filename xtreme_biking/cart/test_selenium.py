import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class CartTest(unittest.TestCase):
    def test_cart_not_empty(self):
        driver = webdriver.Firefox()
        driver.get('http://localhost:8000/cart')
        self.assertNotEqual(driver.find_element(By.TAG_NAME, "a").text, "Tu carrito esta vacío")
        driver.quit()
