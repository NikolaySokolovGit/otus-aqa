import random

from page_objects.catalogue_page import CataloguePage
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage
from page_objects.register_page import RegisterPage


class TestOpencart:
    def test_main_page(self, browser):
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

    def test_product_page(self, browser):
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

    def test_catalogue_page(self, browser):
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

    def test_register_page(self, browser):
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

    def test_login_page(self, browser):
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
