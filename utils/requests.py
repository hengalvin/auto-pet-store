import requests
from utils.logger import logger
from utils.config import TestConfig

base_url = TestConfig.BASE_URL
headers = TestConfig.DEFAULT_HEADERS

def add_pet(payload):
    url = f"{base_url}/pet"
    return create_request_wrapper("post", url, headers=headers, payload=payload)

def get_pet(pet_id):
    url = f"{base_url}/pet/{pet_id}"
    return create_request_wrapper("get", url, headers=headers)

def find_pet_by_status(status):
    url = f"{base_url}/pet/findByStatus"
    return create_request_wrapper("get", url, headers=headers, params={"status": status})


def create_request_wrapper(method: str, url: str, payload=None, headers=None, params=None):
    try:
        logger.info(f"REQUEST: {method.upper()} {url}")
        if payload:
            logger.info(f"Request Payload: {payload}")
        if headers:
            logger.info(f"Request Headers: {headers}")
        if params:
            logger.info(f"Request Params: {params}")

        response = requests.request(method, url, json=payload, headers=headers, params=params)

        # truncate large text
        text_preview = response.text
        if len(text_preview) > 1000:
            text_preview = text_preview[:1000] + "...[truncated]"

        logger.info(f"Response: {response.status_code} {text_preview}")
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        logger.error(f"HTTP {method.upper()} {url} failed with error: {e}")
        raise