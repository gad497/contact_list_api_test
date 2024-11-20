import pytest
import requests
import config

def token_gen():
    url = config.BASE_URL + config.login
    data = {"email": "alex.smith@fake.com", "password": "AlexSmith"}
    response = requests.post(url, json=data)
    return response.json()["token"]


@pytest.fixture
def get_auth():
    return token_gen()


@pytest.fixture
def get_contact():
    token = token_gen()
    url = config.BASE_URL + config.contacts
    header = {"Authorization": token}
    response = requests.get(url, headers=header)
    for contact in response.json():
        if contact["firstName"] == "Lionel" or contact["firstName"] == "Jason":
            return token, contact["_id"]
