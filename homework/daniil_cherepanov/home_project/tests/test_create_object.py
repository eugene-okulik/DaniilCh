import allure
from endpoints.create_object import CreateObject


@allure.title("Создание объекта")
def test_create_object():
    body = {
        "name": "test_object",
        "data": {
            "year": 2025,
            "price": 500
        }
    }

    api = CreateObject()
    api.create_object(body)
    api.should_have_status(200)
    api.should_have_field(["name"], "test_object")
    api.should_have_field(["data", "price"], 500)
