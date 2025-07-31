import os
from locust import HttpUser, between, task


USER_NAME = "denemekullanici"


class WebsiteUser(HttpUser):
    host = os.getenv("TARGET_HOST", "https://petstore.swagger.io")
    wait_time = between(5, 15)

    @task
    def user_create(self):
        payload = {
            "id": 249897,
            "username": USER_NAME,
            "firstName": "deneme",
            "lastName": "kullanici",
            "email": f"{USER_NAME}@gmail.com",
            "password": "123456789",
            "phone": "5962264319",
            "userStatus": 0,
        }
        self.client.post("/v2/user", json=payload)

    @task
    def user_update(self):
        payload = {
            "id": 24985,
            "username": "guncelkullanici",
            "firstName": "guncel",
            "lastName": "kullanici",
            "email": "guncelkullanici@gmail.com",
            "password": "123456",
            "phone": "5952126585",
            "userStatus": 0,
        }
        self.client.put(f"/v2/user/{USER_NAME}", json=payload)

    @task
    def get_user_info(self):
        self.client.get(f"/v2/user/{USER_NAME}")

    @task
    def user_delete(self):
        self.client.delete(f"/v2/user/{USER_NAME}")
