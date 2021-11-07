import pytest
import requests


URL = 'https://jsonplaceholder.typicode.com'


class TestJSONPlaceholder:
    @pytest.mark.parametrize('resource', ('posts', 'comments', 'albums', 'photos', 'todos', 'users'))
    def test_get_resources(self, resource):
        response = requests.get(f'{URL}/{resource}')
        assert response.status_code == 200

    def test_create_post(self):
        data = {
            'title': 'some_title',
            'body': 'some_body',
            'userId': 1
        }
        response = requests.post(f'{URL}/posts', data)
        assert response.status_code == 201

    @pytest.mark.parametrize('route', (
        '/posts/1/comments',
        '/albums/1/photos',
        '/users/1/albums',
        '/users/1/todos',
        '/users/1/posts'
    ))
    def test_get_nested_resources(self, route):
        response = requests.get(f'{URL}{route}')
        assert response.status_code == 200

    @pytest.mark.parametrize('resource', ('posts', 'albums', 'todos'))
    def test_filter_by_user_od(self, resource, user_id=1):
        response = requests.get(f'{URL}/{resource}?userId={user_id}')
        assert all((item['userId'] == user_id for item in response.json()))

    @pytest.mark.parametrize('resource', ('posts', 'comments', 'albums', 'photos', 'todos', 'users'))
    def test_delete_resource(self, resource, resource_id=1):
        response = requests.delete(f'{URL}/{resource}/{resource_id}')
        assert response.status_code == 200
