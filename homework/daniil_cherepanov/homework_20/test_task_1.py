import requests
import pytest

BASE_URL = "http://objapi.course.qa-practice.com/object"


def pytest_sessionstart(session):
    print("Start testing")


def pytest_sessionfinish(session, exitstatus):
    print("Testing completed")


@pytest.fixture(autouse=True)
def around_each_test():
    print("before test")
    yield
    print("after test")


@pytest.fixture
def created_object_id():
    body = {
        "name": "fixture_object",
        "data": {
            "year": 2024,
            "price": 100
        }
    }

    response = requests.post(BASE_URL, json=body)
    assert response.status_code in (200, 201)

    obj_id = response.json()["id"]

    yield obj_id

    requests.delete(f"{BASE_URL}/{obj_id}")


@pytest.mark.critical
@pytest.mark.parametrize(
    "name, year, price",
    [
        ("object_A", 2020, 10),
        ("object_B", 2021, 20),
        ("object_C", 2022, 30),
    ]
)
def test_create_object(name, year, price):
    body = {
        "name": name,
        "data": {
            "year": year,
            "price": price
        }
    }

    response = requests.post(BASE_URL, json=body)

    assert response.status_code in (200, 201)
    data = response.json()

    assert data["name"] == name
    assert data["data"]["year"] == year
    assert data["data"]["price"] == price

    requests.delete(f"{BASE_URL}/{data['id']}")


@pytest.mark.medium
def test_get_object(created_object_id):
    response = requests.get(f"{BASE_URL}/{created_object_id}")

    assert response.status_code == 200
    assert response.json()["id"] == created_object_id


def test_put_object(created_object_id):
    body = {
        "name": "updated_object",
        "data": {
            "year": 2030,
            "price": 999
        }
    }

    response = requests.put(
        f"{BASE_URL}/{created_object_id}",
        json=body
    )

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "updated_object"
    assert data["data"]["year"] == 2030
    assert data["data"]["price"] == 999


def test_patch_object(created_object_id):
    body = {
        "data": {
            "price": 555
        }
    }

    response = requests.patch(
        f"{BASE_URL}/{created_object_id}",
        json=body
    )

    assert response.status_code == 200
    assert response.json()["data"]["price"] == 555


def test_delete_object():
    body = {
        "name": "to_delete",
        "data": {"year": 2000}
    }

    create_resp = requests.post(BASE_URL, json=body)
    assert create_resp.status_code in (200, 201)

    obj_id = create_resp.json()["id"]

    delete_resp = requests.delete(f"{BASE_URL}/{obj_id}")
    assert delete_resp.status_code == 200
