import pytest
import requests
import allure

BASE_URL = "http://objapi.course.qa-practice.com/object"

def pytest_sessionstart(session):
    with allure.step("=== Start testing session ==="):
        print("\n=== Start testing ===")


def pytest_sessionfinish(session, exitstatus):
    with allure.step("=== Testing session finished ==="):
        print("\n=== Testing completed ===")

@pytest.fixture(autouse=True)
def around_each_test():
    with allure.step("=== Before test ==="):
        print("\n--- before test ---")
    yield
    with allure.step("=== After test ==="):
        print("\n--- after test ---")

@pytest.fixture
def created_object_id():
    with allure.step("Создание объекта через фикстуру"):
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

    with allure.step("Удаление объекта после теста через фикстуру"):
        requests.delete(f"{BASE_URL}/{obj_id}")