from http import HTTPStatus
import json
from app.models.User import User, UserUpdate
import requests
import pytest
from random import randint


def test_create_user(app_url, create_user):
	user = create_user
	assert user.status_code == HTTPStatus.CREATED
	User.model_validate(user.json())
	created_user = requests.get(f"{app_url}/api/users/{user.json()['id']}")
	assert created_user.json() == user.json()


def test_update_user_avatar(app_url, create_user):
	user = create_user
	new_avatar = f"https://reqres.in/img/faces/{randint(1, 100)}-image.jpg"
	user_for_update = requests.patch(f"{app_url}/api/users/{user.json()['id']}", data = json.dumps({"avatar": new_avatar}))
	assert user_for_update.status_code == HTTPStatus.OK
	UserUpdate.model_validate(user_for_update.json())
	assert user_for_update.json()['avatar'] == new_avatar
	updated_user = requests.get(f"{app_url}/api/users/{user_for_update.json()['id']}")
	assert updated_user.json()['avatar'] == new_avatar


def test_delete_user(app_url, create_user):
	user = create_user
	user_for_delete = requests.delete(f"{app_url}/api/users/{user.json()['id']}")
	assert user_for_delete.status_code == HTTPStatus.OK
	deleted_user = requests.get(f"{app_url}/api/users/{user.json()['id']}")
	assert deleted_user.status_code == HTTPStatus.NOT_FOUND
	assert deleted_user.json()["detail"] == "User not found"


@pytest.mark.usefixtures("fill_test_data")
def test_get_users(app_url):
    response = requests.get(f"{app_url}/api/users")
    assert response.status_code == HTTPStatus.OK

    user_list = response.json()
    for user in user_list:
        print(user)
        User.model_validate(user)