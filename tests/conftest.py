def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://ya.ru/', help='request url')
    parser.addoption('--status_code', action='store', default=200, help='expected response status code')
