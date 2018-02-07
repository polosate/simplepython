from json import loads, JSONDecodeError
from flask import redirect, url_for, jsonify, abort, request, make_response
from app import app
from models import Task
from database import db_session


def to_json(task):
    return {'id': task.id,
            'name': task.name,
            'description': task.desc,
            'done': task.done}


@app.errorhandler(404)
def not_found(task_id):
    return make_response(jsonify({'error': 'Task {} not found'.format(task_id)}), 404)


@app.errorhandler(400)
def json_parse_error():
    return make_response(jsonify({'error': 'Request is not valid'}), 400)


@app.route("/v1/tasks/")
def get_tasks():
    data = Task.query.all()
    tasks = []
    for t in data:
        tasks.append(to_json(t))
    return jsonify(tasks)


@app.route("/v1/task/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task is None:
        return not_found(task_id)
    return jsonify(to_json(task))


@app.route("/v1/task/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task is None:
        return not_found(task_id)
    try:
        r = loads(request.data)
    except JSONDecodeError:
        return "json parsing error"

    name = r.get("name", None)
    desc = r.get("description", None)
    done = r.get("done", None)

    if name is None and desc is None and done is None:
        return "Nothing to update"

    if name is not None:
        task.name = name
    if desc is not None:
        task.desc = desc
    if done is not None:
        task.done = done
    db_session.commit()
    return make_response(jsonify(True), 200)


@app.route("/v1/task/", methods=["POST"])
def create_task():
    try:
        r = loads(request.data)
        name = r["name"]
        desc = r["description"]
    except (JSONDecodeError, KeyError):
        return json_parse_error()

    new_task = Task(name, desc)
    db_session.add(new_task)
    db_session.commit()
    task_id = new_task.id
    return redirect(url_for('get_task', task_id=task_id))
