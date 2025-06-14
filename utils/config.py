class TestConfig:
    BASE_URL = "https://petstore.swagger.io/v2"
    DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "accept": "application/json",
    }
    RETRY_LIMIT = 5
    RETRY_DELAY = 1  # seconds
