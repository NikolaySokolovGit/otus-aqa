from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def verify_element_presence(self, locator, timeout=1):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(ec.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'Элемент с локатором {locator} не найден за {timeout} с.')
