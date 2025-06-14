import logging
from pathlib import Path

# Create a logs directory if not exists
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Main logger
logger = logging.getLogger("api_test")
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

# File handler for all logs
file_handler = logging.FileHandler(log_dir / "info.log", mode="w")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# File handler for error logs
error_handler = logging.FileHandler(log_dir / "error.log", mode="w")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(error_handler)
