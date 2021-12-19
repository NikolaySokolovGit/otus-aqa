import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=('chrome', 'opera', 'firefox'), default='chrome')
    parser.addoption("--url", action="store", required=True)
    parser.addoption("--admin_username", action="store", required=True)
    parser.addoption("--admin_password", action="store", required=True)


@pytest.fixture
def browser(request):
    driver = request.config.getoption('browser')
    url = request.config.getoption('url')
    url = f'{url}/' if not url.endswith('/') else url

    drivers = {
        'chrome': webdriver.Chrome,
        'opera': webdriver.Opera,
        'firefox': webdriver.Firefox,
    }
    driver = drivers[driver]()

    def finalizer():
        driver.quit()

    request.addfinalizer(finalizer)

    def go_to_path(path=''):
        driver.get(f'{url}{path}')

    driver.open = go_to_path
    driver.open()

    return driver


@pytest.fixture(scope='session')
def admin_user(request):
    user = {
        'username': request.config.getoption('admin_username'),
        'password': request.config.getoption('admin_password')
    }
    return user
