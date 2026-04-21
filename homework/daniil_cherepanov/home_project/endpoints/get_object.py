import allure

from endpoints.base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):

    @allure.step("Получение объекта по id")
    def get_object(self, object_id):
        self._make_request(
            method="GET",
            url=f"{self.base_url}/{object_id}"
        )