import logging
import os
from datetime import datetime

# Only file name
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Only folder path
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Final file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)