"""
Logger utility to configure and retrieve named loggers for the application.
"""

import logging
import os
from datetime import datetime

# Directory where log files will be stored
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# Log file name with today's date
LOG_FILE = os.path.join(
    LOGS_DIR,
    f"log_{datetime.now().strftime('%Y-%m-%d')}.log"
)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def get_logger(name):
    """
    Returns a logger object with the given name and INFO level.

    Args:
        name (str): Name of the logger.

    Returns:
        logging.Logger: Configured logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
