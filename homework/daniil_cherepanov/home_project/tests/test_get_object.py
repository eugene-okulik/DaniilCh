import allure
from endpoints.get_object import GetObject


@allure.title("Получение объекта")
def test_get_object(new_object_id):
    api = GetObject()
    api.get_object(new_object_id)
    api.should_have_status(200)
    api.should_have_field(["id"], new_object_id)
