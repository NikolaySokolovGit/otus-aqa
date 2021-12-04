from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MainPage(BasePage):
    SEARCH_FIELD = (By.CSS_SELECTOR, '#search')
    PRODUCT_LAYOUT = (By.CSS_SELECTOR, '.product-layout')
    CURRENCY_FORM = (By.CSS_SELECTOR, '#form-currency')
    CART = (By.CSS_SELECTOR, '#cart-total')
    MENU = (By.CSS_SELECTOR, '#menu')
    MY_ACCOUNT = (By.CSS_SELECTOR, '.dropdown')
    LOGIN = (By.LINK_TEXT, 'Login')
    REGISTER = (By.LINK_TEXT, 'Register')
    CATALOGUE_DROPDOWN = (By.CSS_SELECTOR, '#menu .dropdown-toggle')
    SEE_ALL = (By.CSS_SELECTOR, '.see-all')

    def go_to_register(self):
        self.driver.find_element(*self.MY_ACCOUNT).click()
        self.driver.find_element(*self.REGISTER).click()

    def go_to_login(self):
        self.driver.find_element(*self.MY_ACCOUNT).click()
        self.driver.find_element(*self.LOGIN).click()

    def go_to_product(self, index):
        self.driver.find_elements(*self.PRODUCT_LAYOUT)[index].click()

    def go_to_catalogue(self, index):
        self.driver.find_elements(*self.CATALOGUE_DROPDOWN)[index].click()
        self.driver.find_element(*self.SEE_ALL).click()
