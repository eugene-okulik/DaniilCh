import allure
from endpoints.put_object import PutObject


@allure.title("Полное обновление объекта")
def test_put_object(new_object_id):
    body = {
        "name": "updated_object",
        "data": {
            "year": 2030,
            "price": 999
        }
    }

    api = PutObject()
    api.update_object(new_object_id, body)
    api.should_have_status(200)
    api.should_have_field(["name"], "updated_object")