from app.errors.errors import UserNotFound, TaskNotFound, TasksNotFound
from models import TTask


class Task(object):
    def __init__(self, task_id, name, desc, done):
        self.task_id = task_id
        self.name = name
        self.desc = desc
        self.done = done

    def to_dict(self):
        return self.__dict__


def get_task(task_id):
    task = TTask.get_records(task_id=task_id)
    if not task:
        raise TaskNotFound(task_id)
    return Task(task[0].task_id, task[0].name, task[0].desc, task[0].done)


def get_tasks(user_id):
    tasks = TTask.get_records(user_id=user_id)
    if not tasks:
        raise TasksNotFound(user_id)
    result = []
    for task in tasks:
        result.append(Task(task.task_id, task.name, task.desc, task.done))
    return result


def create_task(request):
    task_id = TTask.add_record(request["name"], request["description"], request["user_id"])
    if not task_id:
        raise UserNotFound(request["user_id"])
    return task_id

#
# def update_task(**kwargs):
#     return
