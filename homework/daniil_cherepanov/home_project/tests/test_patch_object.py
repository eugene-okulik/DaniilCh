import allure


@allure.title("Частичное обновление объекта")
def test_patch_object(patch_object_endpoint, created_object_id, patch_object_body):
    patch_object_endpoint.patch_object(created_object_id, patch_object_body)

    patch_object_endpoint.check_status_code(200)
    patch_object_endpoint.check_response_field(["name"], "updated_test_object")
