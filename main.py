from flask import Flask, render_template, jsonify
from bp_posts.views import bp_posts
import utils
from logger import create_logger


def create_app(config_path):

    app = Flask(__name__)
    app.register_blueprint(bp_posts)
    app.config.from_pyfile(config_path)
    app.config['JSON_AS_ASCII'] = False
    app.config['JSON_SORT_KEYS'] = False
    return app


app = create_app('config.py')

logger = create_logger()

@app.route('/api/posts/')
def all_posts_api():
    all_posts = utils.load_all_posts_for_api()
    logger.info("Совершен запрос ко всем постам API")
    return jsonify(all_posts)

@app.route('/api/posts/<int:pk>')
def post_api(pk):
    post = utils.get_post_by_pk_for_api(pk)
    logger.info(f"Совершен запрос ко всем посту {pk} API")
    return jsonify(post)

@app.errorhandler(404)
def page_not_found(e):
    logger.error("404 Страница не найдена")
    return "Страница не найдена"

@app.errorhandler(500)
def server_not_response(e):
    logger.error("500 Проблема сервера")
    return "Проблема со связью с сервером"

if __name__ == '__main__':
    logger.info("Приложение запущено")
    app.run(debug=True)
