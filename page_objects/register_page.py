from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from utils import fill_in_the_field


class RegisterPage(BasePage):
    FIRSTNAME_FIELD = (By.CSS_SELECTOR, '#input-firstname')
    LASTNAME_FIELD = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_FIELD = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    REPEAT_PASSWORD = (By.CSS_SELECTOR, '#input-confirm')
    PRIVACY_POLICY = (By.CSS_SELECTOR, '[type="checkbox"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[type="Submit"]')

    def register(self, firstname, lastname, email, telephone, password):
        firstname_field = self.driver.find_element(*self.FIRSTNAME_FIELD)
        lastname_field = self.driver.find_element(*self.LASTNAME_FIELD)
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        telephone_field = self.driver.find_element(*self.TELEPHONE_FIELD)
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        repeat_password_field = self.driver.find_element(*self.REPEAT_PASSWORD)

        fields = (firstname_field, lastname_field, email_field, telephone_field, password_field, repeat_password_field)
        values = (firstname, lastname, email, telephone, password, password)

        for field, value in zip(fields, values):
            fill_in_the_field(field, value)

        privacy_policy = self.driver.find_element(*self.PRIVACY_POLICY)
        privacy_policy.click()
        continue_button = self.driver.find_element(*self.CONTINUE_BUTTON)
        continue_button.click()




