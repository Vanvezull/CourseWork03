import pytest

from bp_posts.dao.comment import Comment
from bp_posts.dao.comment_dao import CommentsDAO

class TestCommentDAO:
    @pytest.fixture
    def comments_dao(self):
        comment_dao_instance = CommentsDAO("./bp_posts/tests/comment_mock.json")
        return comment_dao_instance

    def test_type_of_comment(self, comments_dao):
        """
        Тест того что словарь нужного типа
        :param comments_dao:
        :return:
        """
        comments = comments_dao.get_comments_by_post_id(544)
        assert type(comments) == list

    def test_comment_not_found(self, comments_dao):
        comments = comments_dao.get_comments_by_post_id(544)
        assert comments == []