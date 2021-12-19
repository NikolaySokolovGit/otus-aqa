import pytest
from selenium import webdriver

from database import MariaDB
from utils import db_add_admin_user


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=('chrome', 'opera', 'firefox'), default='chrome')
    parser.addoption("--url", action="store", required=True)
    parser.addoption("--db_url", action="store", default="192.168.0.103:3306")


@pytest.fixture
def browser(request):
    driver = request.config.getoption('browser')
    url = request.config.getoption('url')
    if url is None:
        raise ValueError('Specify')
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
def admin_user(request, username='username', password='admin_password'):
    db_add_admin_user(username, password)

    def delete_admin():
        sql = f"delete from oc_user where username = '{username}'"
        with MariaDB() as db:
            db.execute(sql)

    request.addfinalizer(delete_admin)

    return {'username': username, 'password': password}
