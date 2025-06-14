import pytest
import allure
from utils.requests import get_pet, find_pet_by_status
from utils.status_codes import StatusCode
from utils.config import TestConfig
from schemas.pet import PetResponse

@pytest.mark.flaky(reruns=TestConfig.RETRY_LIMIT, reruns_delay=TestConfig.RETRY_DELAY) 
@allure.title("TC003-Find pet by ID success")
@allure.severity(allure.severity_level.BLOCKER)  # for demo purposes
def test_can_get_pet_by_id():
    # find available pet to get id
    res = find_pet_by_status("available")
    assert res.status_code == StatusCode.SUCCESS
    pet_id = res.json()[0]["id"]

    # find pet by id
    get_pet_res = get_pet(pet_id)
    assert get_pet_res.status_code == StatusCode.SUCCESS
    data = get_pet_res.json()

    # validate response schema
    pet = PetResponse(**data)

    # assertions
    assert pet.id == pet_id
