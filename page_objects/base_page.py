from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    CURRENCY_FORM = (By.CSS_SELECTOR, '#form-currency')
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

    def verify_element_presence(self, locator, timeout=1):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(ec.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'Элемент с локатором {locator} не найден за {timeout} с.')

    def go_to_register(self):
        self.driver.find_element(*self.MY_ACCOUNT).click()
        self.driver.find_element(*self.REGISTER).click()

    def go_to_login(self):
        self.driver.find_element(*self.MY_ACCOUNT).click()
        self.driver.find_element(*self.LOGIN).click()

    def go_to_catalogue(self, index):
        self.driver.find_elements(*self.CATALOGUE_DROPDOWN)[index].click()
        self.driver.find_element(*self.SEE_ALL).click()
