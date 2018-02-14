from hamcrest import assert_that, equal_to

import database
from app import app as application
from tests import populate_db


class TestTask:
    @staticmethod
    def setup_class():
        database.init_db()
        populate_db()
        application.testing = True

    @staticmethod
    def teardown_class():
        pass
        # db_session.remove()
        # Base.metadata.drop_all(bind=test_engine)

    def test_get_task(self):
        r = application.test_client().get('/v1/task/1')
        assert_that(r, equal_to(b'test test test'))
