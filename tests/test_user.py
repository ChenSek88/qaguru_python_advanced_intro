import json
#from .apiclient import test_api
from http import HTTPStatus
import pytest
from faker import Faker
from models.User import User
import requests


fake = Faker()
headers = {"accept": "application/json"}


@pytest.mark.parametrize("user_id", [1, 2, 3, 4])
def test_get_user_by_id_and_validate_user_model(app_url, user_id):
	response = requests.get(f"{app_url}/api/users/{user_id}", headers=headers)
	#response = test_api().get(f"users/{user_id}", headers=headers)
	assert response.status_code == HTTPStatus.OK
	user = json.loads(response.text)
	assert user['id'] == user_id
	User.model_validate(user)


def test_get_nonarchived_users_and_validate_user_model(app_url):
	response = requests.get(f"{app_url}/api/users", headers=headers)
	assert response.status_code == HTTPStatus.OK
	users = response.json()
	for user in users:
		User.model_validate(user)


def test_create_user_and_validate_user_model(app_url):
	new_user = {"name": fake.name(), "email": fake.free_email()}
	response = requests.post(f"{app_url}/api/users", data = json.dumps(new_user))
	assert response.status_code == HTTPStatus.OK
	user = json.loads(response.text)['data']
	User.model_validate(user)


#for example update user name
@pytest.mark.parametrize("user_id", [1, 2])
def test_update_name_user_by_id_and_assert_new_name(app_url, user_id):
	new_name = fake.name()
	response = requests.put(f"{app_url}/api/users/{user_id}?new_name={new_name}", headers=headers)
	assert response.status_code == HTTPStatus.OK
	result = json.loads(response.text)
	assert str(result['data']['name']) == new_name


@pytest.mark.parametrize("user_id", [1, 2])
def test_delete_non_archived_user_by_id(app_url, user_id):
	response = requests.delete(f"{app_url}/api/users/{user_id}",  headers=headers)
	assert response.status_code == HTTPStatus.OK
	result = json.loads(response.text)
	assert result['data']['id'] == user_id