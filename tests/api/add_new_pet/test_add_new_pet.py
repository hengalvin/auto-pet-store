import pytest
from utils.requests import add_pet, get_pet
from utils.tools import load_json
from utils.status_codes import StatusCode
from schemas.pet import PetResponse


payload_path = "../tests/api/add_new_pet/request.json"

@pytest.fixture(params=["Cat1", "Cat2"])
def pet_name(request):
    return request.param

def test_can_add_new_pet(pet_name):
    # load payload and set name
    payload = load_json(payload_path)
    payload["name"] = pet_name

    # create pet with name = pet_name
    add_pet_res = add_pet(payload)
    assert add_pet_res.status_code == StatusCode.SUCCESS  
    data = add_pet_res.json()

    #verify response schema     
    pet = PetResponse(**data)

    # get created pet ID
    pet_id = pet.id

    # verify pet has been created
    get_pet_res = get_pet(pet_id)
    assert get_pet_res.status_code == StatusCode.SUCCESS
    assert get_pet_res.json()["name"] == pet_name # may cause test to fail sometimes, due to API being mocked, pet name to returned always change





