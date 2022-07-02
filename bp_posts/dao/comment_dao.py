import json
from json import JSONDecodeError

from bp_posts.dao.comment import Comment
from exceptions.exceptions import DataSourceError, DataCommentError


class CommentsDAO:

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                post_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f"Не получается получить данные из {self.path}")

        return post_data

    def _load_comments(self):
        comments_data = self._load_data()
        comments = [Comment(**comments_data) for comments_data in comments_data]
        return comments

    def get_comments_by_post_id(self, post_id):
        try:
            comments = self._load_comments()
            comments_match = [comment for comment in comments if comment.post_id == post_id]
        except(ValueError):
            raise DataCommentError(f"Пост не обнаружен")
        return comments_match
