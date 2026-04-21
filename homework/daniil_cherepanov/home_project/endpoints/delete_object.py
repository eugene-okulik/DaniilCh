import allure

from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    @allure.step("Удаление объекта по id")
    def delete_object(self, object_id):
        self._make_request(
            method="DELETE",
            url=f"{self.base_url}/{object_id}"
        )