# vim: ts=4 sw=4 noet
import requests


class ApiClient:
	def __init__(self, base_url):
		self.base_url = base_url


	def post(self, path='/', params=None, data=None, json=None, headers=None):
		url = f"{self.base_url}{path}"
		return requests.post(url=url, params=params, data=data, json=json, headers=headers)

	def get(self, path='/', params=None, headers=None):
		url = f"{self.base_url}{path}"
		return requests.get(url=url, params=params, headers=headers)

	
	def update(self, path='/', params=None, json=None, headers=None):
		url = f"{self.base_url}{path}"
		return requests.put(url=url, params=params, json=json, headers=headers)


	def delete(self, path='/', headers=None):
		url = f"{self.base_url}{path}"
		return requests.delete(url=url, headers=headers)


def test_api():
	return ApiClient(base_url="http://localhost:8000/api/")