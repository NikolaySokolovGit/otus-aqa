from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART = (By.CSS_SELECTOR, '#button-cart')
    LIKE = (By.CSS_SELECTOR, '.fa-heart')
    COMPARE = (By.CSS_SELECTOR, '.fa-exchange')
    QUANTITY = (By.CSS_SELECTOR, '#input-quantity')
    NAV = (By.CSS_SELECTOR, '.nav-tabs')