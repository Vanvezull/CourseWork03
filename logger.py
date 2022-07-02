import logging

def create_logger():

    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")

    file_log = logging.FileHandler("./logs/api.log", encoding="utf-8")
    logger.addHandler(file_log)

    logger_formate = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_log.setFormatter(logger_formate)

    return logger
