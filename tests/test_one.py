class TestOpenCart:
    def test_one(self, browser, pytestconfig):
        url = pytestconfig.getoption('url')
        browser.get(url)
