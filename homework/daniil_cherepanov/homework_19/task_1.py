import requests

# как в посмане базовый URL
BASE_URL = 'http://objapi.course.qa-practice.com/object'


def create_object():
    body = {
        "name": "test_object",
        "data": {
            "year": 2024,
            "price": 100
        }
    }

    response = requests.post(BASE_URL, json=body)

    assert response.status_code == 200, 'Object not created'
    assert response.json()['name'] == body['name']

    return response.json()['id']


def get_one_object():
    object_id = create_object()

    response = requests.get(f'{BASE_URL}/{object_id}')

    assert response.status_code == 200
    assert response.json()['id'] == object_id


def put_object():
    object_id = create_object()

    body = {
        "name": "updated_object",
        "data": {
            "year": 2025,
            "price": 200
        }
    }

    response = requests.put(
        f'{BASE_URL}/{object_id}',
        json=body
    )

    assert response.status_code == 200
    assert response.json()['name'] == body['name']
    assert response.json()['data']['year'] == 2025


def patch_object():
    object_id = create_object()

    body = {
        "data": {
            "price": 999
        }
    }

    response = requests.patch(
        f'{BASE_URL}/{object_id}',
        json=body
    )

    assert response.status_code == 200
    assert response.json()['data']['price'] == 999


def delete_object():
    object_id = create_object()

    response = requests.delete(f'{BASE_URL}/{object_id}')

    assert response.status_code == 200


create_object()
get_one_object()
put_object()
patch_object()
delete_object()
