import logging
from pathlib import Path

# Create a logs directory if not exists
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Custom filter to exclude higher log levels
class MaxLevelFilter(logging.Filter):
    def __init__(self, max_level):
        self.max_level = max_level

    def filter(self, record):
        return record.levelno <= self.max_level

# Main logger
logger = logging.getLogger("api_test")
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

# File handler for info logs only (up to INFO)
file_handler = logging.FileHandler(log_dir / "info.log", mode="w")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
file_handler.addFilter(MaxLevelFilter(logging.WARNING - 1))  # INFO and below

# File handler for error logs only
error_handler = logging.FileHandler(log_dir / "error.log", mode="w")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(error_handler)