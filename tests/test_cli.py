import requests as requests


class TestCLI:
    def test_cli(self, pytestconfig):
        response = requests.get(pytestconfig.getoption('url'))
        assert str(response.status_code) == pytestconfig.getoption('status_code'), f'Запрос по url ' \
                                                                                   f'{pytestconfig.getoption("url")}'
