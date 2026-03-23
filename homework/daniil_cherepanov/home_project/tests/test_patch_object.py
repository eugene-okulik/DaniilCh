import allure
from endpoints.patch_object import PatchObject


@allure.title("Частичное обновление объекта")
def test_patch_object(new_object_id):
    body = {"data": {"price": 555}}

    api = PatchObject()
    api.patch_object(new_object_id, body)

    api.should_have_status(200)
    api.should_have_field(["data", "price"], 555)
