import os
import dotenv
import pytest
import requests
import json

@pytest.fixture(autouse=True, scope="session")
def envs():
	dotenv.load_dotenv()


@pytest.fixture(scope= "session")
def app_url():
	return os.getenv("APP_URL")


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