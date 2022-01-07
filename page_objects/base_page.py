import inspect
import logging
import os

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    CURRENCY_FORM = (By.CSS_SELECTOR, '#form-currency')
    CURRENCY_SELECT = (By.CSS_SELECTOR, '.currency-select')
    CURRENT_CURRENCY = (By.CSS_SELECTOR, '#form-currency strong')
    CART = (By.CSS_SELECTOR, '#cart-total')
    MENU = (By.CSS_SELECTOR, '#menu')
    MY_ACCOUNT = (By.CSS_SELECTOR, '.dropdown')
    LOGIN = (By.LINK_TEXT, 'Login')
    REGISTER = (By.LINK_TEXT, 'Register')
    CATALOGUE_DROPDOWN = (By.CSS_SELECTOR, '#menu .dropdown-toggle')
    SEE_ALL = (By.CSS_SELECTOR, '.see-all')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#search')

    def __init__(self, driver):
        self.driver = driver
        self._cfg_logger()

    def _cfg_logger(self):
        logging.basicConfig(format='%(level)s | %(name)s | %(message)s')
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(logging.INFO)
        os.makedirs('logs', exist_ok=True)
        fh = logging.FileHandler(f"logs/{self.driver.test_name}.log")
        fh.setFormatter(logging.Formatter('%(name)s | %(levelname)s | %(message)s'))
        self.logger.addHandler(fh)

    def verify_element_presence(self, locator, timeout=1):
        self.logger.info(f"Verifying element presence {locator}")
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(ec.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'Элемент с локатором {locator} не найден за {timeout} с.')

    def go_to_register(self):
        self.logger.info("Going to register page")
        self.driver.find_element(*self.MY_ACCOUNT).click()
        self.driver.find_element(*self.REGISTER).click()

    def go_to_login(self):
        self.logger.info("Going to login page")
        self.driver.find_element(*self.MY_ACCOUNT).click()
        self.driver.find_element(*self.LOGIN).click()

    def go_to_catalogue(self, index):
        self.logger.info("Going to catalog")
        self.driver.find_elements(*self.CATALOGUE_DROPDOWN)[index].click()
        self.driver.find_element(*self.SEE_ALL).click()

    def switch_currency(self, index):
        self.logger.info("Switching currency")
        self.driver.find_element(*self.CURRENCY_FORM).click()
        self.driver.find_elements(*self.CURRENCY_SELECT)[index].click()

    def current_currency(self):
        return self.driver.find_element(*self.CURRENT_CURRENCY).text
