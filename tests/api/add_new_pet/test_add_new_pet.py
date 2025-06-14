import pytest
import allure
from utils.requests import add_pet, get_pet
from utils.tools import load_json
from utils.status_codes import StatusCode
from utils.config import TestConfig
from schemas.pet import PetResponse


payload_path = "../tests/api/add_new_pet/request.json"

@pytest.mark.flaky(reruns=TestConfig.RETRY_LIMIT, reruns_delay=TestConfig.RETRY_DELAY) 
@pytest.mark.parametrize("pet_name", ["Cat1", "Cat2"])
@allure.title("TC001-Add new pet with custom name success")
@allure.severity(allure.severity_level.CRITICAL)  # for demo purposes
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

