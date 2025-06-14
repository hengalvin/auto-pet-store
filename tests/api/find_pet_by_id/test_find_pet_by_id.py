import pytest
from utils.requests import get_pet
from utils.status_codes import StatusCode
from schemas.pet import PetResponse
from utils.tools import log_response

@pytest.fixture(params=[9223372036854740750])
def id(request):
    return request.param

def test_can_get_pet_by_id(id):
    # find pet by id
    get_pet_res = get_pet(id)
    assert get_pet_res.status_code == StatusCode.SUCCESS
    data = get_pet_res.json()

    # validate response schema
    pet = PetResponse(**data)

    # assertions
    assert pet.id == id
