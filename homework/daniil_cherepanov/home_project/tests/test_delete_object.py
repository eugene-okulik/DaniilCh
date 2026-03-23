import allure
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject


@allure.title("Удаление объекта")
def test_delete_object():
    body = {"name": "to_delete", "data": {"year": 2000}}

    creator = CreateObject().create_object(body)
    obj_id = creator.response_json["id"]

    api = DeleteObject()
    api.delete_object(obj_id)
    api.should_have_status(200)
