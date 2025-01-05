from app import app
from models import db, Contacts
from faker import Factory

BASE_URL= "http://localhost:5000"

def setup_module(module):
    pass


def teardown_module(module):
    pass

def test_get_contacts(client):
    response = client.get(BASE_URL + "/api/contacts")
    assert response.status_code in [200,201]
    assert isinstance(response.get_json(), list)

def test_post_contact(client):
    new_contact = {
        "name": "new",
        "surname": "new",
        "email": "new@new.com",
        "phone": "0505505050"
    }
    response = client.post(f"{BASE_URL}/api/contacts", json = new_contact)
    assert response.status_code in [200,201]
    response_data = response.get_json()
    assert response_data["name"] == new_contact["name"]
    assert response_data["surname"] == new_contact["surname"]
    assert response_data["email"] == new_contact["email"]
    assert response_data["phone"] == new_contact["phone"]


def test_post_missing_data_contact(client):
    incomplete_contact = {
        "name": "incomplete",
        "surname": "incomplete"
    }
    response = client.post(f"{BASE_URL}", json=incomplete_contact)
    assert response.status_code == 404

def test_post_contact_with_extra_fields(client):
    new_contact = {
        "name": "new",
        "surname": "new",
        "email": "new1@new.com",
        "phone": "001-476-367-2806",
        "extra": "extra"
    }
    response = client.post(f"{BASE_URL}/api/contacts", json=new_contact)
    assert response.status_code != 200

# def test_post_empty_payload(client):
#     response = client.post(f"{BASE_URL}/api/contacts", json={})
#     assert response.status_code in [400,401,404,403] 
    