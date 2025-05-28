# utils/logger.py

import logging
import sys

def setup_logger():
    logger = logging.getLogger("parameter_mapper")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)

    return logger

logger = setup_logger()