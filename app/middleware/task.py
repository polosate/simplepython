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
    task = TTask.query.filter_by(task_id=task_id).first()
    if not task:
        return None
    return Task(task.task_id, task.name, task.desc, task.done)


def get_tasks(user_id):
    tasks = TTask.query.filter_by(user_id=user_id).all()
    if not len(tasks):
        return None
    result = []
    for task in tasks:
        result.append(Task(task.task_id, task.name, task.desc, task.done))
    return result


def create_task(name, desc, user_id):
    task_id = TTask.add_record(name, desc, user_id)
    if not task_id:
        return "User {} not found".format(user_id)
    return task_id


def update_task(**kwargs):
    return
