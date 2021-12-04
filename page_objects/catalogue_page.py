from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CataloguePage(BasePage):
    LIST_BUTTON = (By.CSS_SELECTOR, '.fa-th-list')
    GRID_BUTTON = (By.CSS_SELECTOR, '.fa-th')
    SORT = (By.CSS_SELECTOR, '#input-sort')
    LIMIT = (By.CSS_SELECTOR, '#input-limit')
    PRODUCT_LAYOUT = (By.CSS_SELECTOR, '.product-layout')