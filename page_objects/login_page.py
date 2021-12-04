from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
    ACCOUNT_LINK = (By.LINK_TEXT, 'Account')
