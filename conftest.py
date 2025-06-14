import pytest
from datetime import datetime
from utils.logger import logger

@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    # BEFORE ALL
    start_time = datetime.now()
    logger.info(f"===== TEST SESSION STARTED at {start_time} =====")

    yield

    # TEARDOWN
    end_time = datetime.now()
    logger.info(f"===== TEST SESSION ENDED at {end_time} =====")
