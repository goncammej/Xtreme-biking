import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000/cart')

    def tearDown(self):
        self.driver.quit()

    def test_cart_not_empty(self):
        self.assertNotEqual(self.driver.find_element(By.TAG_NAME, "a").text, "Tu carrito:")
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "El carrito está vacío")

    def test_navigation_elements(self):
        logo_element = self.driver.find_element(By.XPATH, "//img[@alt='xtreme-logo']")
        self.assertTrue(logo_element.is_displayed(), "El logo no está presente en la página")

        login_link = self.driver.find_element(By.XPATH, "//a[@href='/accounts/login/']")
        signup_link = self.driver.find_element(By.XPATH, "//a[@href='/accounts/signup/']")
        self.assertTrue(login_link.is_displayed(), "El enlace de inicio de sesión no está presente en la página")
        self.assertTrue(signup_link.is_displayed(), "El enlace de registro no está presente en la página")

        navigation_links = self.driver.find_elements(By.XPATH, "//ul[@class='flex flex-row font-medium mt-0 space-x-8 rtl:space-x-reverse text-sm']//a")
        self.assertGreater(len(navigation_links), 0, "No se encontraron enlaces de navegación en la página")

        search_form = self.driver.find_element(By.XPATH, "//form[@action='/store/search/']")
        self.assertTrue(search_form.is_displayed(), "El formulario de búsqueda no está presente en la página")

    def test_cart_empty(self):
        driver = webdriver.Firefox()
        driver.get('http://localhost:8000/cart')
        self.assertNotEqual(driver.find_element(By.TAG_NAME, "a").text, "Pagar")
