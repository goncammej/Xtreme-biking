import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class ClientTest(unittest.TestCase):
    def test_login(self):
        driver = webdriver.Firefox()
        driver.get('http://localhost:8000/client/dashboard')
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "Inicia sesión en tu cuenta")
        self.assertNotEqual(driver.find_element(By.TAG_NAME, "a").text, "Registrate ")

        driver.quit()
