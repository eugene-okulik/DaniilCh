import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    def delete_object(self, obj_id):
        with allure.step("Удаление объекта (DELETE)"):
            self.response = requests.delete(f"{self.BASE_URL}/{obj_id}")
        return self