import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class PutObject(BaseEndpoint):

    def update_object(self, obj_id, body):
        with allure.step("Полное обновление объекта (PUT)"):
            self.response = requests.put(f"{self.BASE_URL}/{obj_id}", json=body)
            self.response_json = self.response.json()
        return self
