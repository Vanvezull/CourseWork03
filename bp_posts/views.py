
from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import abort

from bp_posts.dao.comment_dao import CommentsDAO
from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS
from bp_posts.dao.post_dao import PostDAO
from logger import create_logger

bp_posts = Blueprint("bp_posts", __name__, template_folder="templates")


post_dao = PostDAO(DATA_PATH_POSTS)
comments_dao = CommentsDAO(DATA_PATH_COMMENTS)

logger = create_logger("bp_log")


@bp_posts.route('/')
def posts_index():
    """
    Вывод ленты всех постов
    :return:
    """
    all_posts = post_dao.get_all_posts()
    return render_template('posts_index.html', posts=all_posts)

@bp_posts.route('/posts/<int:pk>')
def single_post(pk):
    """
    Вывод поста по Pk
    :param pk:
    :return:
    """
    post = post_dao.get_post_by_pk(pk)
    comments = comments_dao.get_comments_by_post_id(pk)

    if post is None:
        abort(404)

    logger.info(f"Выполнен поиск поста по id : {pk}")

    return render_template('posts_single_post.html', post=post, comments=comments, comments_len=len(comments))

@bp_posts.route('/users/<string:poster_name>')
def posts_by_user(poster_name):
    """
    Вывод ленты постов пользователя
    :param poster_name:
    :return:
    """
    posts = post_dao.get_by_user(poster_name)
    logger.info(f"Выполнен поиск по пользователю {poster_name}")
    return render_template('posts_user-feed.html', posts=posts, user_name=poster_name)

@bp_posts.route('/search/')
def posts_by_search():

    """
    Поиск по ключевому слову
    :return:
    """

    user_search = request.args.get('s', '')

    if user_search == "":
        posts = []
    else:
        posts = post_dao.search_in_content(user_search)

    return render_template('posts_search.html', posts=posts, user_search=user_search, posts_len=len(posts))


