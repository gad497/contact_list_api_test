import pytest
import requests
import config

def test_get_contacts(get_auth):
    url = config.BASE_URL + config.contacts
    header = {"Authorization": get_auth}
    response = requests.get(url, headers=header)
    assert response.status_code == 200

def test_add_contact(get_auth):
    url = config.BASE_URL + config.contacts
    header = {"Authorization": get_auth}
    response = requests.post(url, headers=header, json=config.data)
    assert response.status_code == 201

def test_get_contact(get_contact):
    url = config.BASE_URL + config.contacts + "/" + get_contact[1]
    header = {"Authorization": get_contact[0]}
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    assert response.json()["firstName"] == "Lionel"

def test_update_contact(get_contact):
    url = config.BASE_URL + config.contacts + "/" + get_contact[1]
    header = {"Authorization": get_contact[0]}
    response = requests.put(url, headers=header, json=config.new_data)
    assert response.status_code == 200
    response = requests.get(url, headers=header)
    json_data = response.json()
    assert json_data["firstName"] == config.new_data["firstName"]
    assert json_data["lastName"] == config.new_data["lastName"]

def test_delete_contact(get_contact):
    url = config.BASE_URL + config.contacts + "/" + get_contact[1]
    header = {"Authorization": get_contact[0]}
    response = requests.delete(url, headers=header)
    assert response.status_code == 200
    response = requests.get(url, headers=header)
    assert response.status_code == 404

@pytest.mark.negetive
def test_get_contacts_without_token():
    url = config.BASE_URL + config.contacts
    response = requests.get(url)
    assert response.status_code == 401
    assert response.json()["error"] == "Please authenticate."

@pytest.mark.negetive
def test_get_contact_not_found(get_auth):
    url = config.BASE_URL + config.contacts + "/" + "66b48c49db58fd0013d05d7b"
    header = {"Authorization": get_auth}
    response = requests.delete(url, headers=header)
    assert response.status_code == 404
