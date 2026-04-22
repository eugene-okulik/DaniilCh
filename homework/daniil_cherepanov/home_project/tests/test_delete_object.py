import allure


@allure.title("Удаление объекта")
def test_delete_object(delete_object_endpoint, created_object_id):
    delete_object_endpoint.delete_object(created_object_id)

    delete_object_endpoint.check_status_code(200)
    delete_object_endpoint.check_response_field(
        ["message"],
        f"Object with id = {created_object_id} has been deleted."
    )
