import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):

    def create_object(self, body):
        with allure.step("Создание объекта (POST)"):
            self.response = requests.post(self.BASE_URL, json=body)
            self.response_json = self.response.json()
        return self
