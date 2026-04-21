import allure


@allure.title("Полное обновление объекта")
def test_put_object(put_object_endpoint, created_object_id, put_object_body):
    put_object_endpoint.put_object(created_object_id, put_object_body)

    put_object_endpoint.check_status_code(200)
    put_object_endpoint.check_response_field(["name"], "replaced_test_object")
    put_object_endpoint.check_response_field(["data", "year"], 2026)
    put_object_endpoint.check_response_field(["data", "price"], 700)
