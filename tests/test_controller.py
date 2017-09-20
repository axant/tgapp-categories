import tg
from tgext.pluggable import app_model
from .base import configure_app, create_app, flush_db_changes
import re
from webtest import AppError
find_urls = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')


class RegistrationControllerTests(object):
    def setup(self):
        self.app = create_app(self.app_config, False)

    def test_index(self):
        resp = self.app.get('/')
        assert 'HELLO' in resp.text

    def test_tgappcategories_index(self):
        resp = self.app.get('/tgappcategories', extra_environ={'REMOTE_USER': 'manager'})

        assert '/new_category' in resp.text, resp

    def test_new_category_form(self):
        resp = self.app.get('/tgappcategories/new_category', extra_environ={'REMOTE_USER': 'manager'})

        assert 'name="name"' in resp.text, resp
        assert 'name="description"' in resp.text, resp
        assert '/create_category' in resp.text, resp

    def test_tgappcategories_auth(self):
        try:
            self.app.get('/tgappcategories')
        except AppError as e:
            assert '401' in str(e)


class TestRegistrationControllerSQLA(RegistrationControllerTests):
    @classmethod
    def setupClass(cls):
        cls.app_config = configure_app('sqlalchemy')


class TestRegistrationControllerMing(RegistrationControllerTests):
    @classmethod
    def setupClass(cls):
        cls.app_config = configure_app('ming')