import logging

def create_logger(name):
    """
    Создание логгера
    :return:
    """

    logger = logging.getLogger(name)
    logger.setLevel("DEBUG")
    """
    Задаем логгеру файл для логов
    """
    file_log = logging.FileHandler("./logs/api.log", encoding="utf-8")
    logger.addHandler(file_log)
    """
    Указываем в каком формате должны быть логи
    """
    logger_formate = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_log.setFormatter(logger_formate)

    return logger
