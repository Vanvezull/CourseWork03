from main import app

class TestAPI:
    def test_api_posts(self):
        """
        Тест того что API посты список и не пустые
        :return:
        """
        resp = app.test_client().get('/api/posts', follow_redirects=True)
        assert resp.status_code == 200
        assert type(resp.json) == list
        assert len(resp.json) != 0

    def test_api_post(self):
        """
        Тест конкретного поста API
        :return:
        """
        resp = app.test_client().get('/api/posts/1', follow_redirects=True)
        assert resp.status_code == 200
        assert type(resp.json) == dict
        assert resp.json.keys() == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}