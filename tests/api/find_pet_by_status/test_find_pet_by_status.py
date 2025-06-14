import pytest
import allure
from utils.requests import find_pet_by_status
from utils.status_codes import StatusCode
from utils.config import TestConfig
from schemas.pet import PetResponse

@pytest.mark.flaky(reruns=TestConfig.RETRY_LIMIT, reruns_delay=TestConfig.RETRY_DELAY) 
@pytest.mark.parametrize("status", ["available", "pending"])
@allure.title("TC002-Find pet by status success")
@allure.severity(allure.severity_level.NORMAL) # for demo purposes
def test_can_find_pet_by_status(status):
    # find pet by status
    find_pet_res = find_pet_by_status(status)
    assert find_pet_res.status_code == StatusCode.SUCCESS
    pet_list = find_pet_res.json()

    # validate schema & status for all pets in response
    pets = [PetResponse(**pet) for pet in pet_list]
    for pet in pets:
        assert pet.status == status
