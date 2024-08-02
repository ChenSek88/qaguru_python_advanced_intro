from http import HTTPStatus
import json
from faker import Faker
from app.models.User import User, UserUpdate
import requests
from random import randint
import pytest


fake = Faker()


def create_user(app_url):
	new_user = {
		"first_name": fake.first_name(),
		"last_name": fake.last_name(),
		"avatar": f"https://reqres.in/img/faces/{randint(1, 100)}-image.jpg",
		"email": fake.free_email()}
	response = requests.post(f"{app_url}/api/users", data=json.dumps(new_user))
	assert response.status_code == HTTPStatus.CREATED
	return response


def test_create_user_and_validate_user_model(app_url):
	user = create_user(app_url)
	assert user.status_code == HTTPStatus.CREATED
	User.model_validate(user.json())


def test_update_user_avatar_by_id_and_assert_new_avatar(app_url):
	new_avatar = f"https://reqres.in/img/faces/{randint(1, 100)}-image.jpg"
	user_id = create_user(app_url).json()['id']
	response = requests.patch(f"{app_url}/api/users/{user_id}", data = json.dumps({"avatar": new_avatar}))
	assert response.status_code == HTTPStatus.OK
	user = json.loads(response.text)
	UserUpdate.model_validate(user)
	assert user['avatar'] == new_avatar


def test_delete_user_by_id_and_get_user_not_found(app_url):
	user_id = create_user(app_url).json()['id']
	response = requests.delete(f"{app_url}/api/users/{user_id}")
	assert response.status_code == HTTPStatus.OK
	response = requests.get(f"{app_url}/api/users/{user_id}")
	response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.usefixtures("fill_test_data")
def test_get_users(app_url):
    response = requests.get(f"{app_url}/api/users")
    assert response.status_code == HTTPStatus.OK

    user_list = response.json()
    for user in user_list:
        print(user)
        User.model_validate(user)



