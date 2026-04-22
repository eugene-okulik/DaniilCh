import allure

from endpoints.base_endpoint import BaseEndpoint


class PutObject(BaseEndpoint):

    @allure.step("Полное обновление объекта")
    def put_object(self, object_id, body):
        self._make_request(
            method="PUT",
            url=f"{self.base_url}/{object_id}",
            json=body
        )
