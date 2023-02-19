import json
from typing import Dict, List

import requests
import logging
from assertpy import assert_that
import pytest


def test_post():
    url_0 = "https://rahulshettyacademy.com//maps/api/place/add/json?qaclick123"
    post_data = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        }, "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": [
            "shoe park",
            "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
    }
    response = requests.post(url_0, post_data)
    res = response.json()

    assert_that(res).contains_value("Frontline house")


def test_get():
    url_0 = "https://rahulshettyacademy.com//maps/api/place/get/json?qaclick123"
    response = requests.get(url_0)
    assert_that(response).is_equal_to(200)


def test_put():
    url_0 = "https://rahulshettyacademy.com//maps/api/place/update/json?qaclick123"
    response = requests.put(url_0, {"name": "Frontline houseNew"})
    assert_that(response).contains_value("Frontline houseNew")

def test_del():
    url_0 = "https://rahulshettyacademy.com//maps/api/place/delete/json?qaclick123"
    response = requests.delete(url_0)
    assert_that(response).does_not_contain_value("Frontline houseNew")

