import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class StoreTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000/store/catalogue/')

    def tearDown(self):
        self.driver.quit()

    def test_store(self):
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h2").text, "Todos los productos")

    def test_product_page_elements(self):
        title_element = self.driver.find_element(By.XPATH, "//h2[contains(text(), 'Todos los productos')]")
        self.assertTrue(title_element.is_displayed(), "El título 'Todos los productos' no está presente en la página")

        product_elements = self.driver.find_elements(By.XPATH, "//div[@class='group relative overflow-hidden mt-8 flex flex-col justify-between']")
        self.assertGreater(len(product_elements), 0, "No se encontraron productos en la página")
