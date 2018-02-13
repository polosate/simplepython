from hamcrest import assert_that, equal_to
from app import app as application
from tests import fixtures
from models import TTask, TUser
from database import db_session, engine, init_db, Base


def population_db():
    for user in fixtures.users:
        new_user = TUser(user_id=user["user_id"],
                         first_name=user["first_name"],
                         last_name=user["last_name"])
        db_session.add(new_user)
        db_session.commit()
    for task in fixtures.tasks:
        new_user = TTask(user_id=task["user_id"],
                         task_id=task["task_id"],
                         name=task["name"],
                         desc=task["desc"])
        db_session.add(new_user)
        db_session.commit()


class TestTask:
    @staticmethod
    def setup_class():
        init_db()
        population_db()
        application.testing = True

    @staticmethod
    def teardown_class():
        db_session.remove()
        # Base.metadata.drop_all(bind=engine)

    def test_get_task(self):
        r = application.test_client().get('/v1/task/1')
        assert_that(r, equal_to(b'test test test'))
