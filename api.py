import requests
import allure
from faker import Faker


class ApiClient:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"
    REGISTER = f"{BASE_URL}/auth/register"
    USER = f"{BASE_URL}/auth/user"

    @staticmethod
    def user_data():
        fake = Faker()
        return {
            "email": fake.email(),
            "password": fake.password(length=8),
            "name": fake.first_name()
        }

    def create_account(self, data):
        response = requests.post(self.REGISTER, json=data).json()
        token = response["accessToken"]
        return token

    def delete_user(self, token):
        return requests.delete(self.USER, headers={"Authorization": token})
