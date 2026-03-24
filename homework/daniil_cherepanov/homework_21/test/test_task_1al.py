import requests
import pytest
import allure

BASE_URL = "http://objapi.course.qa-practice.com/object"


@allure.feature("Objects API")
@allure.story("Create object")
@allure.title("Создание объекта с разными параметрами")
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

    with allure.step("Отправка POST запроса"):
        response = requests.post(BASE_URL, json=body)

    with allure.step("Проверка кода ответа"):
        assert response.status_code in (200, 201)

    data = response.json()

    with allure.step("Валидация тела ответа"):
        assert data["name"] == name
        assert data["data"]["year"] == year
        assert data["data"]["price"] == price

    with allure.step("Удаление созданного объекта"):
        requests.delete(f"{BASE_URL}/{data['id']}")


@allure.story("Get object")
@allure.title("Получение объекта по ID")
@pytest.mark.medium
def test_get_object(created_object_id):
    with allure.step("Отправка GET запроса"):
        response = requests.get(f"{BASE_URL}/{created_object_id}")

    with allure.step("Проверка кода ответа и ID объекта"):
        assert response.status_code == 200
        assert response.json()["id"] == created_object_id


@allure.story("Update object (PUT)")
@allure.title("Полное обновление объекта")
def test_put_object(created_object_id):
    body = {
        "name": "updated_object",
        "data": {
            "year": 2030,
            "price": 999
        }
    }

    with allure.step("Отправка PUT запроса"):
        response = requests.put(f"{BASE_URL}/{created_object_id}", json=body)

    with allure.step("Проверка кода ответа"):
        assert response.status_code == 200

    data = response.json()
    with allure.step("Валидация обновлённого объекта"):
        assert data["name"] == "updated_object"
        assert data["data"]["year"] == 2030
        assert data["data"]["price"] == 999


@allure.story("Partial update (PATCH)")
@allure.title("Частичное обновление объекта")
def test_patch_object(created_object_id):
    body = {"data": {"price": 555}}

    with allure.step("Отправка PATCH запроса"):
        response = requests.patch(f"{BASE_URL}/{created_object_id}", json=body)

    with allure.step("Проверка кода ответа и обновлённого поля"):
        assert response.status_code == 200
        assert response.json()["data"]["price"] == 555


@allure.story("Delete object")
@allure.title("Удаление объекта")
def test_delete_object():
    body = {"name": "to_delete", "data": {"year": 2000}}

    with allure.step("Создание объекта для удаления"):
        create_resp = requests.post(BASE_URL, json=body)
        assert create_resp.status_code in (200, 201)
        obj_id = create_resp.json()["id"]

    with allure.step("Удаление объекта"):
        delete_resp = requests.delete(f"{BASE_URL}/{obj_id}")
        assert delete_resp.status_code == 200
