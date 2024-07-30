import json
from http import HTTPStatus
import pytest
from models.User import User, PaginationResponse
import requests


@pytest.mark.parametrize("size", [1, 6, 12])
def test_pagination_with_size(app_url, size):
    response = requests.get(f"{app_url}/api/users/?size={size}&page=1")
    assert response.status_code == HTTPStatus.OK
    result = PaginationResponse.model_validate(response.json())
    assert len(result.items) == size
    assert result.pages == (result.total + size - 1) // size


@pytest.mark.parametrize("page", [1, 6, 12])
def test_pagination_with_page(app_url, page):
    response = requests.get(f"{app_url}/api/users/?size=1&page={page}")
    assert response.status_code == HTTPStatus.OK
    result = PaginationResponse.model_validate(response.json())
    assert result.page == page


@pytest.mark.parametrize("page, size", [(1, 6), (6, 1)])
def test_pagination_with_page_and_size(app_url, size, page):
    response = requests.get(f"{app_url}/api/users/?size={size}&page={page}")
    assert response.status_code == HTTPStatus.OK
    result = PaginationResponse.model_validate(response.json())
    assert len(result.items) == size
    assert result.page == page


def test_different_data_with_different_pages(app_url):
    response1 = requests.get(f"{app_url}/api/users/?size=1&page=1")
    response2 = requests.get(f"{app_url}/api/users/?size=1&page=2")
    assert response1.status_code == HTTPStatus.OK
    assert response2.status_code == HTTPStatus.OK
    result1 = PaginationResponse.model_validate(response1.json())
    result2 = PaginationResponse.model_validate(response2.json())
    assert result1.items != result2.items


@pytest.mark.parametrize("page, size", [(0, 0), (0, -1), (-1, 0)])
def test_pagination_with_invalid_page_and_size(app_url, size, page):
    response = requests.get(f"{app_url}/api/users/?size={size}&page={page}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY