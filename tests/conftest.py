import os
import dotenv
import pytest
import requests
import json
from faker import Faker
from random import randint
from http import HTTPStatus


fake = Faker()


@pytest.fixture(autouse=True, scope="session")
def envs():
	dotenv.load_dotenv()


@pytest.fixture(scope= "session")
def app_url():
	return os.getenv("APP_URL")


@pytest.fixture()
def create_user(app_url):
    new_user = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "avatar": f"https://reqres.in/img/faces/{randint(1, 100)}-image.jpg",
        "email": fake.free_email()}
    user = requests.post(f"{app_url}/api/users", data=json.dumps(new_user))
    assert user.status_code == HTTPStatus.CREATED
    return user


@pytest.fixture(scope="module")
def fill_test_data(app_url):
    with open("users.json") as f:
        test_data_users = json.load(f)
    api_users = []
    for user in test_data_users:
        response = requests.post(f"{app_url}/api/users", json=user)
        api_users.append(response.json())

    user_ids = [user["id"] for user in api_users]

    yield user_ids

    for user_id in user_ids:
        requests.delete(f"{app_url}/api/users/{user_id}")