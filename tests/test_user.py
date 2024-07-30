import json
from http import HTTPStatus
import pytest
from faker import Faker
from models.User import User
import requests
from random import randint


fake = Faker()
headers = {"accept": "application/json"}


@pytest.mark.parametrize("user_id", [1, 2, 3, 4])
def test_get_user_by_id_assert_and_validate_user_model(app_url, user_id):
	response = requests.get(f"{app_url}/api/users/{user_id}", headers=headers)
	assert response.status_code == HTTPStatus.OK
	user = json.loads(response.text)
	assert user['id'] == user_id
	User.model_validate(user)


def test_get_nonarchived_users_and_validate_user_model(app_url):
	response = requests.get(f"{app_url}/api/users", headers=headers)
	assert response.status_code == HTTPStatus.OK
	users = response.json()
	for user in users['items']:
		User.model_validate(user)


def test_create_user_and_validate_user_model(app_url):
	new_user = {
		"first_name": fake.first_name(), 
		"last_name": fake.last_name(), 
		"avatar": f"https://reqres.in/img/faces/{randint(1,100)}-image.jpg", 
		"email": fake.free_email()}
	response = requests.post(f"{app_url}/api/users", data = json.dumps(new_user))
	assert response.status_code == HTTPStatus.OK
	user = json.loads(response.text)['data']
	User.model_validate(user)


@pytest.mark.parametrize("user_id", [1, 2])
def test_update_user_name_by_id_and_assert_new_name(app_url, user_id):
	new_name = fake.first_name()
	response = requests.put(f"{app_url}/api/users/{user_id}?new_name={new_name}", headers=headers)
	assert response.status_code == HTTPStatus.OK
	result = json.loads(response.text)
	assert result['data']['first_name'] == new_name


@pytest.mark.parametrize("user_id", [1])
def test_delete_non_archived_user_by_id_and_assert_id(app_url, user_id):
	response = requests.delete(f"{app_url}/api/users/{user_id}",  headers=headers)
	assert response.status_code == HTTPStatus.OK
	result = json.loads(response.text)
	assert result['data']['id'] == user_id