import json

import requests
from assertpy import assert_that


def test_get():
    url_0 = "https://fakerestapi.azurewebsites.net/api/v1/Books"
    response = requests.get(url_0)
    assert_that(response.status_code).is_equal_to(200)


def test_post():
    url_0 = "https://fakerestapi.azurewebsites.net/api/v1/Books"
    body = {
        "id": 6,
        "title": "string",
        "description": "string",
        "pageCount": 6,
        "excerpt": "string",
        "publishDate": "2023-03-09T14:38:15.567Z"
    }
    response = requests.post(url_0, json=body)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains_value("string")


def test_put():
    url_0 = "https://fakerestapi.azurewebsites.net/api/v1/Books/6"
    body = {
        "id": 7,
        "title": "string",
        "description": "string",
        "pageCount": 6,
        "excerpt": "string",
        "publishDate": "2023-03-09T14:38:15.567Z"
    }
    response = requests.put(url_0, json=body)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains_value(7)
    response2 = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Books/7")
    assert_that(response2.status_code).is_equal_to(200)


def test_delete():
    url_0 = "https://fakerestapi.azurewebsites.net/api/v1/Books/7"
    data = "2023-03-09T14:38:15.567Z"
    response = requests.delete(url_0, data=data)
    assert_that(response.status_code).is_equal_to(200)
    response2 = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Books/7")
    assert_that(response2.json()).does_not_contain_value("2023-03-09T14:38:15.567Z")








