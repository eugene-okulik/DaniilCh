import allure

from endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):

    @allure.step("Создание объекта")
    def create_object(self, body):
        self._make_request(
            method="POST",
            url=self.base_url,
            json=body
        )
