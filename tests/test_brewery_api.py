import pytest
import requests

from schemas.brewery_schemas import BreweryList

URL = 'https://api.openbrewerydb.org/'


class TestBreweryAPI:
    def test_list_breweries(self):
        response = requests.get(f'{URL}/breweries')
        assert response.status_code == 200
        BreweryList.parse_obj(response.json())

    @pytest.mark.parametrize('city', ('san_diego', 'MOSCOW', 'new%20york', 'Budapest'))
    def test_filter_by_city(self, city):
        response = requests.get(f'{URL}/breweries?by_city={city}')
        assert response.status_code == 200
        assert all((brewery['city'].lower() == city.lower().replace('_', ' ').replace('%20', ' ')
                    for brewery in response.json()))

    @pytest.mark.parametrize('name', ('Beer', 'DOG', 'cider'))
    def test_filter_by_name(self, name):
        response = requests.get(f'{URL}/breweries?by_name={name}')
        assert response.status_code == 200
        assert all((name.lower() in brewery['name'].lower() for brewery in response.json()))

    def test_filter_by_type(self, brewery_type='nano'):
        response = requests.get(f'{URL}/breweries?by_type={brewery_type}')
        assert response.status_code == 200
        assert all((brewery['brewery_type'] == brewery_type for brewery in response.json()))

    def test_per_page(self, per_page=15):
        response = requests.get(f'{URL}/breweries?per_page={per_page}')
        assert response.status_code == 200
        assert len(response.json()) == per_page
