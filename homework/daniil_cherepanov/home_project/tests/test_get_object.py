import allure


@allure.title("Получение объекта по id")
def test_get_object(get_object_endpoint, created_object_id):
    get_object_endpoint.get_object(created_object_id)

    get_object_endpoint.check_status_code(200)
    get_object_endpoint.check_response_field(["id"], created_object_id)