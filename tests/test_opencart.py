from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestOpencart:
    product_url = 'index.php?route=product/product&path=20&product_id=42'
    catalogue_url = 'index.php?route=product/category&path=20'
    register_url = 'index.php?route=account/register'
    login_url = 'index.php?route=account/login'

    def test_main_page(self, browser, pytestconfig):
        url = pytestconfig.getoption('url')
        browser.get(url)
        wait = WebDriverWait(browser, 3)
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#search')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.product-layout')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#form-currency')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#cart-total')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#menu')))

    def test_product_page(self, browser, pytestconfig):
        url = f'{pytestconfig.getoption("url")}{self.product_url}'
        browser.get(url)
        wait = WebDriverWait(browser, 3)
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#button-cart')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.fa-heart')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.fa-exchange')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#input-quantity')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.nav-tabs')))

    def test_catalogue_page(self, browser, pytestconfig):
        url = f'{pytestconfig.getoption("url")}{self.catalogue_url}'
        browser.get(url)
        wait = WebDriverWait(browser, 3)
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.fa-th-list')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.fa-th')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#input-sort')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#input-limit')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.product-layout')))

    def test_register_page(self, browser, pytestconfig):
        url = f'{pytestconfig.getoption("url")}{self.register_url}'
        browser.get(url)
        wait = WebDriverWait(browser, 3)
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#input-firstname')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#input-lastname')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#input-email')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#input-telephone')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#input-password')))

    def test_login_page(self, browser, pytestconfig):
        url = f'{pytestconfig.getoption("url")}{self.register_url}'
        browser.get(url)
        wait = WebDriverWait(browser, 3)
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#input-email')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#input-password')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '[type="submit"]')))
        wait.until(ec.presence_of_element_located((By.LINK_TEXT, 'Forgotten Password')))
        wait.until(ec.presence_of_element_located((By.LINK_TEXT, 'Account')))
