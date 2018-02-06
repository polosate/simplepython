import names
from flask import redirect, url_for, jsonify, json
from app import app
from models import Task
from database import db_session


def to_json(task):
    return {'id': task.id,
            'name': task.name,
            'description': task.desc,
            'done': task.done}


@app.route("/v1/tasks/")
def get_tasks():
    data = Task.query.all()
    tasks = []
    for t in data:
        tasks.append(to_json(t))
    return jsonify(tasks)


@app.route("/v1/task/<int:task_id>", methods=["GET", "PUT"])
def get_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    return jsonify(to_json(task))


@app.route("/v1/task/", methods=["GET"])
def create_task():
    new_task = Task(names.get_first_name(), names.get_full_name())
    db_session.add(new_task)
    db_session.commit()
    task_id = new_task.id
    return redirect(url_for('get_task', task_id=task_id))
