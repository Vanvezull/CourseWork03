import json
from json import JSONDecodeError

from exceptions.exceptions import DataSourceError
from logger import create_logger

logger = create_logger("utils_log")

def load_all_posts_for_api():
    """
    Вывод всех постов в API
    :return:
    """
    try:
        with open('./data/posts.json', "r", encoding="utf-8") as file:
            post_data = json.load(file)
    except(FileNotFoundError, JSONDecodeError):
        raise DataSourceError(f"Не получается получить данные из файла")

    logger.info("Выполнен запрос api/posts")
    return post_data

def get_post_by_pk_for_api(pk):
    """
    Вывод одного поста API по pk
    :param pk:
    :return:
    """

    if type(pk) != int:
        raise TypeError("pk должен быть числом")

    posts = load_all_posts_for_api()
    for post in posts:
        if post["pk"] == pk:
            logger.info(f"Выполнен запрос api/posts/{pk}")
            return post
