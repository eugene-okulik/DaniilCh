import allure
import requests

from utils.logger import log_request, log_response


class BaseEndpoint:
    base_url = "https://api.restful-api.dev/objects"

    def __init__(self):
        self.response = None
        self.response_json = None

    def _make_request(self, method, url, **kwargs):
        log_request(method, url, **kwargs)
        self.response = requests.request(method, url, **kwargs)
        log_response(self.response)

        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = None

    def check_status_code(self, status_code):
        with allure.step(f"Проверка статус-кода: {status_code}"):
            assert self.response.status_code == status_code, (
                f"Expected status code is {status_code}, "
                f"but actual is {self.response.status_code}"
            )

    def check_response_field(self, field_path, expected_value):
        with allure.step(f"Проверка значения поля {field_path}"):
            data = self.response_json
            for key in field_path:
                data = data[key]
            assert data == expected_value, (
                f"Expected value for field {field_path} is {expected_value}, "
                f"but actual is {data}"
            )

    def check_field_exists(self, field_name):
        with allure.step(f"Проверка наличия поля {field_name} в ответе"):
            assert field_name in self.response_json, (
                f"Field '{field_name}' is not present in response"
            )