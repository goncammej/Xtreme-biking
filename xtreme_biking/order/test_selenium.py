import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class OrderTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000/order/search/')

    def tearDown(self):
        self.driver.quit()

    def test_order_search(self):
        search_input = self.driver.find_element(By.ID, 'Search')

        search_button = self.driver.find_element(By.TAG_NAME, 'button')

        self.assertTrue(search_input.is_displayed(), "El campo de búsqueda no está presente")
        self.assertTrue(search_button.is_displayed(), "El botón de búsqueda no está presente")

