from database import db_session
from models import TTask


class Task(object):
    def __init__(self, id, name, desc, done):
        self.id = id
        self.name = name
        self.desc = desc
        self.done = done

    def to_dict(self):
        return self.__dict__


def get_task(**kwargs):
    if not kwargs.get("task_id"):
        result = []
        tasks = TTask.query.all()
        for task in tasks:
            result.append(Task(task.id, task.name, task.desc, task.done))
    else:
        task = TTask.query.filter_by(id=kwargs.get("task_id")).first()
        result = Task(task.id, task.name, task.desc, task.done)
    return result


def create_task(name, desc):
    new_task = TTask(name, desc)
    db_session.add(new_task)
    db_session.commit()
    return new_task.id


def update_task(**kwargs):
    return
