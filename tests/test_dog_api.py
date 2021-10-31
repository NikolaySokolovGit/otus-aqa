import pytest
import requests

URL = 'https://dog.ceo/api/'


class TestDogAPI:
    def test_single_random_image(self):
        """DISPLAY SINGLE RANDOM IMAGE FROM ALL DOGS COLLECTION"""
        response = requests.get(f'{URL}breeds/image/random')
        assert response.status_code == 200
        assert response.json().get('message')

    @pytest.mark.parametrize('number, expected', ((1, 1), (50, 50), (-1, 1), (0, 1), (51, 50)))
    def test_multiple_random_image(self, number, expected):
        """DISPLAY MULTIPLE RANDOM IMAGES FROM ALL DOGS COLLECTION"""
        response = requests.get(f'{URL}breeds/image/random/{number}')
        assert response.status_code == 200
        assert len(response.json().get('message')) == expected

    def test_single_random_breed(self, breed='akita'):
        """Returns a random dog image from a breed, e.g. hound"""
        response = requests.get(f'{URL}breed/{breed}/images/random')
        assert response.status_code == 200
        assert breed in response.json().get('message')

    @pytest.mark.parametrize('number, expected', ((1, 1), (9, 9), (10, 9), (0, 1), (-1, 9)))
    def test_multiple_random_breed(self, number, expected):
        """Return multiple random dog image from a breed, e.g. hound"""
        response = requests.get(f'{URL}breed/akita/images/random/{number}')
        assert response.status_code == 200
        assert len(response.json().get('message')) == expected

    def test_single_random_sub_breed(self, breed='hound', sub='afghan'):
        """SINGLE RANDOM IMAGE FROM A SUB BREED COLLECTION"""
        response = requests.get(f'{URL}breed/{breed}/{sub}/images/random')
        assert response.status_code == 200
        assert f"{breed}-{sub}" in response.json().get('message')
