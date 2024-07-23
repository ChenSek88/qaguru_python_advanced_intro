import json
from .conftest import *


headers = {"accept": "application/json"}


def get_user_by_id(user_id):
	response = test_api().get("users/" + user_id, headers=headers)
	result = json.loads(response.text)
	if response.status_code == 200:
		assert str(result[0]['id']) == user_id
		return result[0]['id']
	else:
		assert response.status_code == 404


def create_user(name, email, age):
	new_user = "name=%s&email=%s&age=%s" %(name, email, age)
	response = test_api().post("users/?" + new_user)
	result = json.loads(response.text)
	assert response.status_code == 200
	assert str(result['data']['name']) == name


#for example update user name
def update_user_by_id(user_id, name):
	new_name = "?new_name=%s" % name
	response = test_api().update("users/" + user_id + new_name, headers=headers)
	result = json.loads(response.text)
	assert response.status_code == 200
	assert str(result['data']['name']) == name


def delete_user_by_id(user_id):
	result = get_user_by_id(user_id)
	if result:
		response = test_api().delete("users/" + user_id,  headers=headers)
		result = json.loads(response.text)
		assert response.status_code == 200
		assert str(result['data']['id']) == user_id
	else:
		assert result == None


def get_users():
	response = test_api().get("users", headers=headers)
	assert response.status_code == 200
