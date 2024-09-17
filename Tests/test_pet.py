import requests

BASE_URL = "https://petstore.swagger.io/v2"


def create_pet(pet_id, name, status="available"):
    pet_data = {
        "id": pet_id,
        "name": name,
        "status": status
    }
    response = requests.post(f"{BASE_URL}/pet", json=pet_data)
    return response

def test_create_pet_positive():
    response = create_pet(1234, "Doggo")
    assert response.status_code == 200, "Pet creation failed"
    data = response.json()
    assert data['id'] == 1234
    assert data['name'] == "Doggo"
    assert data['status'] == "available"

def test_create_pet_negative():
    invalid_pet_data = {
        "id": "invalid_id",
        "name": 12345,
        "status": "unknown_status"
    }
    response = requests.post(f"{BASE_URL}/pet", json=invalid_pet_data)
    assert response.status_code == 500, "Should fail due to invalid data"


def test_read_pet_positive():
    create_pet(1234, "Doggo")
    response = requests.get(f"{BASE_URL}/pet/1234")
    assert response.status_code == 200, "Failed to get pet details"
    data = response.json()
    assert data['id'] == 1234
    assert data['name'] == "Doggo"


def test_read_pet_negative():
    response = requests.get(f"{BASE_URL}/pet/999999")
    assert response.status_code == 404, "Pet should not exist"

def test_update_pet_positive():
    create_pet(1234, "Doggo")
    updated_pet_data = {
        "id": 1234,
        "name": "DoggoUpdated",
        "status": "sold"
    }
    response = requests.put(f"{BASE_URL}/pet", json=updated_pet_data)
    assert response.status_code == 200, "Failed to update pet details"
    data = response.json()
    assert data['name'] == "DoggoUpdated"
    assert data['status'] == "sold"


def test_update_pet_negative():
    invalid_pet_data = {
        "id": 'aaa',
        "name": 123,
        "status": "unknown_status"
    }
    response = requests.put(f"{BASE_URL}/pet", json=invalid_pet_data)
    assert response.status_code == 500, "Should fail due to invalid data"


def test_delete_pet_positive():
    create_pet(1234, "Doggo")
    response = requests.delete(f"{BASE_URL}/pet/1234")
    assert response.status_code == 200, "Failed to delete pet"
    response = requests.get(f"{BASE_URL}/pet/1234")
    assert response.status_code == 404, "Pet should not exist after deletion"


def test_delete_pet_negative():
    response = requests.delete(f"{BASE_URL}/pet/777777")
    assert response.status_code == 404, "Pet should not exist, deletion should fail"
