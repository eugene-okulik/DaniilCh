import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):

    def get_object(self, obj_id):
        with allure.step("Получение объекта (GET)"):
            self.response = requests.get(f"{self.BASE_URL}/{obj_id}")
            self.response_json = self.response.json()
        return self
