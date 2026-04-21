import allure

from endpoints.base_endpoint import BaseEndpoint


class PatchObject(BaseEndpoint):

    @allure.step("Частичное обновление объекта")
    def patch_object(self, object_id, body):
        self._make_request(
            method="PATCH",
            url=f"{self.base_url}/{object_id}",
            json=body
        )
