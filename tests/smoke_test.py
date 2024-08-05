from http import HTTPStatus
import requests


def test_app_status(app_url):
    response = requests.get(f"{app_url}/status")
    assert response.status_code == HTTPStatus.OK
    assert response.json()['database'] is True


def test_microservice_is_running(app_url):
    response = requests.get(f"{app_url}/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "FastAPI microservice is running"}