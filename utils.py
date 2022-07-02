import json
from json import JSONDecodeError

from exceptions.exceptions import DataSourceError
from logger import create_logger

logger = create_logger()


def load_all_posts_for_api():
    try:
        with open('./data/posts.json', "r", encoding="utf-8") as file:
            post_data = json.load(file)
    except(FileNotFoundError, JSONDecodeError):
        raise DataSourceError(f"Не получается получить данные из файла")

    logger.info("Выполнен запрос api/posts")
    return post_data

def get_post_by_pk_for_api(pk):

    if type(pk) != int:
        raise TypeError("pk должен быть числом")

    posts = load_all_posts_for_api()
    for post in posts:
        if post["pk"] == pk:
            logger.info(f"Выполнен запрос api/posts/{pk}")
            return post
