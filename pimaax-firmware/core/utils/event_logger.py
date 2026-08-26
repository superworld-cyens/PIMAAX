import logging
import os
from datetime import datetime


def logger(log_id, log_dir="./logs", log_filename="event.log", log_level=logging.INFO):
    #init logger
    logger = logging.getLogger(log_id)
    logger.setLevel(log_level)

    if logger.hasHandlers():
        logger.handlers.clear()

    #printing console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    ))
    logger.addHandler(console_handler)

    #file handler for saving logs to a file
    os.makedirs(log_dir, exist_ok=True)
    file_path = os.path.join(log_dir, log_filename)
    file_handler = logging.FileHandler(file_path)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    ))
    logger.addHandler(file_handler)

    return logger
