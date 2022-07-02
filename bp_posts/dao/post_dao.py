import json
from json import JSONDecodeError

from bp_posts.dao.post import Post
from exceptions.exceptions import DataSourceError
from logger import create_logger

logger = create_logger()

class PostDAO:

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                post_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            logger.error(f"Не получается получить данные из {self.path}")
            raise DataSourceError(f"Не получается получить данные из {self.path}")

        return post_data

    def _load_posts(self):

        post_data = self._load_data()
        list_posts = [Post(**post_data) for post_data in post_data]
        return list_posts

    def get_all_posts(self):
        posts = self._load_posts()
        return posts

    def get_post_by_pk(self, pk):

        if type(pk) != int:
            raise TypeError("pk должен быть числом")

        posts = self._load_posts()
        for post in posts:
            if post.pk == pk:
                return post

    def search_in_content(self, substring):

        substring = str(substring).lower()
        posts = self._load_posts()
        matching_posts = [post for post in posts if substring in post.content.lower()]

        return matching_posts

    def get_by_user(self, user_name):

        user_name = str(user_name).lower()
        posts = self._load_posts()
        matching_posts = [post for post in posts if post.poster_name.lower() == user_name]

        return matching_posts
