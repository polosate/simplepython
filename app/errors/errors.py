class UserNotFound(Exception):
    msg = ""

    def __init__(self, user_id):
        self.msg = "User {} not found".format(user_id)

    def __str__(self):
        return repr(self.msg)


class TaskNotFound(Exception):
    def __init__(self, task_id):
        self.msg = "Task {} not found".format(task_id)

    def __str__(self):
        return repr(self.msg)


class TasksNotFound(Exception):
    def __init__(self, user_id):
        self.msg = "Tasks for user {} not found".format(user_id)

    def __str__(self):
        return repr(self.msg)