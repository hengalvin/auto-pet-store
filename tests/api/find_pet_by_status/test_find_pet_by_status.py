import pytest
from utils.requests import find_pet_by_status
from utils.status_codes import StatusCode
from schemas.pet import PetResponse

@pytest.mark.flaky(reruns=5, reruns_delay=1) #flaky test, retry when fail
@pytest.mark.parametrize("status", ["available", "pending"])
def test_can_find_pet_by_status(status):
    # find pet by status
    find_pet_res = find_pet_by_status(status)
    assert find_pet_res.status_code == StatusCode.SUCCESS
    pet_list = find_pet_res.json()

    # validate schema & status for all pets in response
    pets = [PetResponse(**pet) for pet in pet_list]
    for pet in pets:
        assert pet.status == status
