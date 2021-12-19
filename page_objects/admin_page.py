from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils import fill_in_the_field


class AdminPage:
    PATH = '/admin'
    USERNAME = (By.CSS_SELECTOR, '#input-username')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    SUBMIT = (By.CSS_SELECTOR, '.btn')
    CATALOG = (By.CSS_SELECTOR, '#menu-catalog')
    PRODUCTS = (By.LINK_TEXT, 'Products')
    PLUS = (By.CSS_SELECTOR, '.fa-plus')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name1')
    META_TAG_TITLE = (By.CSS_SELECTOR, '#input-meta-title1')
    DATA = (By.LINK_TEXT, 'Data')
    MODEL = (By.CSS_SELECTOR, '#input-model')
    SAVE = (By.CSS_SELECTOR, '[type="submit"]')
    SUCCESS = (By.CSS_SELECTOR, '.alert-success')
    PRODUCT_CHECKBOX = (By.CSS_SELECTOR, 'tbody tr [type="checkbox"]')
    DELETE_BTN = (By.CSS_SELECTOR, '.btn-danger')

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.open(self.PATH)

    def login(self, username, password):
        username_field = self.driver.find_element(*self.USERNAME)
        password_field = self.driver.find_element(*self.PASSWORD)

        elements = (username_field, password_field)
        values = (username, password)

        for element, value in zip(elements, values):
            fill_in_the_field(element, value)

        submit_btn = self.driver.find_element(*self.SUBMIT)
        submit_btn.click()

    def go_to_products(self, timeout=2):
        wait = WebDriverWait(self.driver, timeout)
        for elem in (self.CATALOG, self.PRODUCTS):
            try:
                wait.until(ec.element_to_be_clickable(elem)).click()
            except TimeoutException:
                raise AssertionError(f'Элемент с локатором {elem} не найден за {timeout} с.')

    def add_product(self, product_name, meta_tag, model):
        self.driver.find_element(*self.PLUS).click()
        product_name_field = self.driver.find_element(*self.PRODUCT_NAME)
        meta_tag_field = self.driver.find_element(*self.META_TAG_TITLE)
        for elem, value in zip((product_name_field, meta_tag_field), (product_name, meta_tag)):
            fill_in_the_field(elem, value)
        self.driver.find_element(*self.DATA).click()
        model_field = self.driver.find_element(*self.MODEL)
        fill_in_the_field(model_field, model)
        self.driver.find_element(*self.SAVE).click()

    def select_product(self, index):
        self.driver.find_elements(*self.PRODUCT_CHECKBOX)[index].click()

    def delete_product(self):
        self.driver.find_element(*self.DELETE_BTN).click()
        alert = self.driver.switch_to.alert
        alert.accept()
