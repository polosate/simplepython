from tests import fixtures
from models import TTask, TUser
from database import db_session


def populate_db():
    for user in fixtures.users:
        new_user = TUser(user_id=user["user_id"],
                         first_name=user["first_name"],
                         last_name=user["last_name"])
        db_session.add(new_user)
        db_session.commit()

        # TUser.add_record(first_name=user["first_name"],
        #                  last_name=user["last_name"])
    for task in fixtures.tasks:
        new_user = TTask(user_id=task["user_id"],
                         task_id=task["task_id"],
                         name=task["name"],
                         desc=task["desc"])
        db_session.add(new_user)
        db_session.commit()

        # TTask.add_record(task["name"], task["desc"], task["user_id"])