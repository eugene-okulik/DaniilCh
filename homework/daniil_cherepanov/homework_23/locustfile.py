from locust import HttpUser, task, between
import random


class ObjectUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.object_ids = []

        with self.client.get("/object", catch_response=True) as response:
            if response.status_code == 200:
                try:
                    data = response.json()
                    if isinstance(data, list):
                        self.object_ids = [obj["id"] for obj in data]
                        response.success()
                    else:
                        response.failure("Response is not a list")
                except Exception as e:
                    response.failure(f"JSON error: {e}")
            else:
                response.failure(f"Failed to get objects: {response.status_code}")

    @task(2)
    def get_all_objects(self):
        with self.client.get("/object", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Status code: {response.status_code}")
            else:
                try:
                    data = response.json()
                    if not isinstance(data, list):
                        response.failure("Response is not a list")
                    else:
                        response.success()
                except Exception as e:
                    response.failure(f"JSON error: {e}")

    @task(4)
    def get_random_object(self):
        if not self.object_ids:
            return

        obj_id = random.choice(self.object_ids)

        with self.client.get(f"/object/{obj_id}", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Failed to get object {obj_id}")
            else:
                try:
                    data = response.json()
                    if data.get("id") != obj_id:
                        response.failure("Wrong object returned")
                    else:
                        response.success()
                except Exception as e:
                    response.failure(f"JSON error: {e}")

    @task(1)
    def create_object(self):
        payload = {
            "name": f"test_{random.randint(1, 10000)}",
            "data": {"value": random.randint(1, 100)}
        }

        with self.client.post("/object", json=payload, catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to create object")
            else:
                try:
                    obj = response.json()
                    if "id" not in obj:
                        response.failure("No id in response")
                    else:
                        self.object_ids.append(obj["id"])
                        response.success()
                except Exception as e:
                    response.failure(f"JSON error: {e}")

    @task(1)
    def delete_object(self):
        if not self.object_ids:
            return

        obj_id = random.choice(self.object_ids)

        with self.client.delete(f"/object/{obj_id}", catch_response=True) as response:
            if response.status_code not in [200, 204]:
                response.failure(f"Failed to delete {obj_id}")
            else:
                self.object_ids.remove(obj_id)
                response.success()
