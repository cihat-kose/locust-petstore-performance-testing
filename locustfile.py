import os
from locust import HttpUser, task, between


class PetstoreUser(HttpUser):
    host = os.getenv("HOST", "https://petstore.swagger.io")
    wait_time = between(float(os.getenv("WAIT_TIME_MIN", 1)), float(os.getenv("WAIT_TIME_MAX", 5)))

    username = os.getenv("USERNAME", "locustuser")

    @task
    def user_create(self):
        payload = {
            "id": 249897,
            "username": self.username,
            "firstName": "Locust",
            "lastName": "User",
            "email": "locustuser@example.com",
            "password": "123456789",
            "phone": "5555555555",
            "userStatus": 0,
        }
        self.client.post("/v2/user", json=payload)

    @task
    def user_update(self):
        payload = {
            "id": 249897,
            "username": self.username,
            "firstName": "Updated",
            "lastName": "User",
            "email": "locustuser@example.com",
            "password": "123456789",
            "phone": "5555555555",
            "userStatus": 0,
        }
        self.client.put(f"/v2/user/{self.username}", json=payload)

    @task
    def get_user_info(self):
        self.client.get(f"/v2/user/{self.username}")

    @task
    def user_delete(self):
        self.client.delete(f"/v2/user/{self.username}")
