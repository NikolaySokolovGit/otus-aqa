from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MainPage(BasePage):
    PRODUCT_LAYOUT = (By.CSS_SELECTOR, '.product-layout')

    def go_to_product(self, index):
        self.logger.info(f"Going to product #{index}")
        self.driver.find_elements(*self.PRODUCT_LAYOUT)[index].click()
