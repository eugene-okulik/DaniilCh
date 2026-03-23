import allure


class Assertions:

    @staticmethod
    def status_code(response, expected_code):
        with allure.step(f"Проверка статус-кода == {expected_code}"):
            assert response.status_code == expected_code

    @staticmethod
    def field_value(response_json, field_path, expected_value):
        with allure.step(f"Проверка поля {field_path} == {expected_value}"):
            data = response_json
            for key in field_path:
                data = data[key]
            assert data == expected_value