import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class PatchObject(BaseEndpoint):

    def patch_object(self, obj_id, body):
        with allure.step("Частичное обновление объекта (PATCH)"):
            self.response = requests.patch(f"{self.BASE_URL}/{obj_id}", json=body)
            self.response_json = self.response.json()
        return self