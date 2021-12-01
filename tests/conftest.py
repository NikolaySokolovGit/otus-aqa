import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=('chrome', 'opera', 'firefox'), default='chrome')
    parser.addoption("--url", action="store")


@pytest.fixture
def browser(request):
    driver = request.config.getoption('browser')
    drivers = {
        'chrome': webdriver.Chrome,
        'opera': webdriver.Opera,
        'firefox': webdriver.Firefox,
    }
    driver = drivers[driver]()

    def finalizer():
        driver.quit()

    request.addfinalizer(finalizer)

    return driver
