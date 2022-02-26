import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=('chrome', 'opera', 'firefox'), default='chrome')
    parser.addoption("--browser_ver", action="store", default=None)
    parser.addoption("--url", action="store", required=True)
    parser.addoption("--admin_username", action="store", required=True)
    parser.addoption("--admin_password", action="store", required=True)
    parser.addoption("--executor", action="store", default="192.168.0.102")


@pytest.fixture
def browser(request):
    driver = request.config.getoption('browser')
    executor = request.config.getoption("executor")
    browser_ver = request.config.getoption("browser_ver")
    url = request.config.getoption('url')
    url = f'{url}/' if not url.endswith('/') else url

    if executor == 'local':
        drivers = {
            'chrome': webdriver.Chrome,
            'opera': webdriver.Opera,
            'firefox': webdriver.Firefox,
        }
        driver = drivers[driver]()
    else:
        caps = {
            "browserName": driver,
        }
        if browser_ver is not None:
            caps["version"] = browser_ver
        executor_url = f"http://{executor}:4444/wd/hub"
        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)

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
