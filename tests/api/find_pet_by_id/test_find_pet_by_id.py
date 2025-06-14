import pytest
from utils.requests import get_pet, find_pet_by_status
from utils.status_codes import StatusCode
from schemas.pet import PetResponse


@pytest.fixture
def id():
    # Dynamically fetch an available pet ID
    res = find_pet_by_status("available")
    assert res.status_code == StatusCode.SUCCESS
    pet_id = res.json()[0]["id"]
    return pet_id

def test_can_get_pet_by_id(id):
    # find pet by id
    get_pet_res = get_pet(id)
    assert get_pet_res.status_code == StatusCode.SUCCESS
    data = get_pet_res.json()

    # validate response schema
    pet = PetResponse(**data)

    # assertions
    assert pet.id == id
