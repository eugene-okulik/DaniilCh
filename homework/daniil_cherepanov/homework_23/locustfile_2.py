from locust import HttpUser, task, between
import random


class ObjectUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.object_ids = []

        response = self.client.get("/object")
        if response.status_code == 200:
            data = response.json()
            self.object_ids = [obj["id"] for obj in data]

    @task(2)
    def get_all_objects(self):
        self.client.get("/object")

    @task(4)
    def get_random_object(self):
        if self.object_ids:
            obj_id = random.choice(self.object_ids)
            self.client.get(f"/object/{obj_id}")

    @task(1)
    def create_object(self):
        payload = {
            "name": f"test_{random.randint(1, 10000)}",
            "data": {"value": random.randint(1, 100)}
        }

        response = self.client.post("/object", json=payload)

        if response.status_code == 200:
            obj = response.json()
            self.object_ids.append(obj["id"])

    @task(1)
    def delete_object(self):
        if self.object_ids:
            obj_id = random.choice(self.object_ids)
            self.object_ids.remove(obj_id)
            self.client.delete(f"/object/{obj_id}")
