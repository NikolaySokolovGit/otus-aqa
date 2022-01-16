import random

import allure
import pytest
import selenium.common.exceptions
from faker import Faker

from page_objects.admin_page import AdminPage
from page_objects.base_page import BasePage
from page_objects.catalogue_page import CataloguePage
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage
from page_objects.register_page import RegisterPage


fake = Faker()


class TestOpencart:
    @allure.title('Check elements on main page')
    def test_main_page(self, browser):
        browser.test_name = "main_page"
        page = MainPage(browser)
        elements_to_check = (
            page.SEARCH_FIELD,
            page.CART,
            page.CURRENCY_FORM,
            page.PRODUCT_LAYOUT,
            page.MENU,
        )
        for locator in elements_to_check:
            page.verify_element_presence(locator)

    @allure.title('Checking elements on product page')
    def test_product_page(self, browser):
        browser.test_name = "product_page"
        MainPage(browser).go_to_product(random.randint(0, 3))
        page = ProductPage(browser)
        elements_to_check = (
            page.LIKE,
            page.COMPARE,
            page.ADD_TO_CART,
            page.QUANTITY,
            page.NAV,
        )
        for locator in elements_to_check:
            page.verify_element_presence(locator)

    @allure.title('Checking elements on catalog page')
    def test_catalogue_page(self, browser):
        browser.test_name = "catalog_page"
        MainPage(browser).go_to_catalogue(0)
        page = CataloguePage(browser)
        elements_to_check = (
            page.SORT,
            page.PRODUCT_LAYOUT,
            page.LIMIT,
            page.GRID_BUTTON,
            page.LIST_BUTTON,
        )
        for locator in elements_to_check:
            page.verify_element_presence(locator)

    @allure.title('Checking elements on register page')
    def test_register_page(self, browser):
        browser.test_name = "register_page"
        MainPage(browser).go_to_register()
        page = RegisterPage(browser)
        elements_to_check = (
            page.PASSWORD_FIELD,
            page.EMAIL_FIELD,
            page.FIRSTNAME_FIELD,
            page.LASTNAME_FIELD,
            page.TELEPHONE_FIELD,
        )
        for locator in elements_to_check:
            page.verify_element_presence(locator)

    @allure.title('Checking elements on login page')
    def test_login_page(self, browser):
        browser.test_name = "login_page"
        MainPage(browser).go_to_login()
        page = LoginPage(browser)
        elements_to_check = (
            page.PASSWORD_FIELD,
            page.EMAIL_FIELD,
            page.ACCOUNT_LINK,
            page.FORGOTTEN_PASSWORD,
            page.SUBMIT_BUTTON,
        )
        for locator in elements_to_check:
            page.verify_element_presence(locator)

    @allure.title('Registration')
    def test_registration(self, browser):
        browser.test_name = "registration"
        try:
            BasePage(browser).go_to_register()
            RegisterPage(browser).register(fake.word(), fake.word(), fake.email(), fake.phone_number(), fake.password())
        except selenium.common.exceptions.NoSuchElementException as e:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'Элемент не найден: {e.msg}')
        assert browser.current_url.endswith('account/success')

    @allure.title('Switching currency')
    @pytest.mark.parametrize('index, currency', ((0, '€'), (1, '£'), (2, '$')))
    def test_switch_currency(self, browser, index, currency):
        browser.test_name = "switch_currency"
        page = BasePage(browser)
        try:
            page.switch_currency(index)
        except selenium.common.exceptions.NoSuchElementException as e:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'Элемент не найден: {e.msg}')

        assert page.current_currency() == currency

    @allure.title('Add product')
    def test_add_product(self, browser, admin_user):
        browser.test_name = "add product"
        page = AdminPage(browser)
        try:
            page.open()
            page.login(**admin_user)
            page.go_to_products()
            page.add_product('sample', 'smp', 'sample')
            browser.find_element(*page.SUCCESS)
        except selenium.common.exceptions.NoSuchElementException as e:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'Элемент не найден: {e.msg}')

    @allure.title('Delete product')
    def test_delete_product(self, browser, admin_user):
        browser.test_name = "delete product"
        page = AdminPage(browser)
        try:
            page.open()
            page.login(**admin_user)
            page.go_to_products()
            page.add_product('delete', 'dlt', 'delete')
            page.select_product(0)
            page.delete_product()
            browser.find_element(*page.SUCCESS)
        except selenium.common.exceptions.NoSuchElementException as e:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'Элемент не найден: {e.msg}')
