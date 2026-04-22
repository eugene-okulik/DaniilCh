import allure

from fixtures.object_fixtures import CREATE_OBJECT_BODY


@allure.title("Создание объекта")
def test_create_object(create_object_endpoint):
    create_object_endpoint.create_object(CREATE_OBJECT_BODY)

    create_object_endpoint.check_status_code(200)
    create_object_endpoint.check_response_field(["name"], "test_object")
    create_object_endpoint.check_response_field(["data", "year"], 2025)
    create_object_endpoint.check_response_field(["data", "price"], 500)
    create_object_endpoint.check_field_exists("id")