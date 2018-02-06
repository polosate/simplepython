from flask import redirect, url_for
from app import app
from models import Task
from database import db_session


@app.route("/v1/tasks/")
def get_tasks():
    return "All tasks"


@app.route("/v1/task/<int:task_id>", methods=["GET", "PUT"])
def get_task(task_id):
    task = Task.query.filter(Task.id == task_id).first()
    return task


@app.route("/v1/task/", methods=["GET"])
def create_task():
    new_task = Task("Read the book", "M.Lutts Learning Python")
    db_session.add(new_task)
    db_session.commit()
    task_id = new_task.id
    return redirect(url_for('get_task', task_id=task_id))
