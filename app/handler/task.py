from json import loads, JSONDecodeError
from jsonschema import validate, ValidationError

from flask import redirect, url_for, jsonify, request, make_response

from app import app
from app.middleware import task
from app.errors.errors import UserNotFound, TaskNotFound, TasksNotFound
from app.schemas.task import task_schema


@app.route("/v1/tasks/<int:user_id>/")
def get_tasks(user_id):
    try:
        tasks = task.get_tasks(user_id)
    except TasksNotFound as e:
        return not_found(e.msg)
    return jsonify([t.to_dict() for t in tasks])


@app.route("/v1/task/<int:task_id>/", methods=["GET"])
def get_task(task_id):
    try:
        t = task.get_task(task_id)
    except TaskNotFound as e:
        return not_found(e.msg)
    return jsonify(t.to_dict())


@app.route("/v1/task/", methods=["POST"])
def create_task():
    try:
        data = loads(request.data)
        validate(data, task_schema)
    except JSONDecodeError as e:
        return json_parse_error(e.msg)
    except ValidationError as e:
        return json_parse_error(e.msg)

    try:
        task_id = task.create_task(data)
    except UserNotFound as e:
        return not_found(e.msg)
    return redirect(url_for('get_task', task_id=task_id))

# @app.route("/v1/task/<int:task_id>", methods=["PUT"])
# def update_task(task_id):
#     task = Task.query.filter_by(id=task_id).first()
#     if task is None:
#         return not_found(task_id)
#     try:
#         r = loads(request.data)
#     except JSONDecodeError:
#         return "json parsing error"
#
#     name = r.get("name", None)
#     desc = r.get("description", None)
#     done = r.get("done", None)
#
#     if name is None and desc is None and done is None:
#         return "Nothing to update"
#
#     if name is not None:
#         task.name = name
#     if desc is not None:
#         task.desc = desc
#     if done is not None:
#         task.done = done
#     db_session.commit()
#     return make_response(jsonify(True), 200)
#


@app.errorhandler(404)
def not_found(message):
    return make_response(jsonify({'error': 'Not Found',
                                  'message': message}),
                         404)


@app.errorhandler(400)
def json_parse_error(message):
    return make_response(jsonify({'error': 'Request is not valid',
                                  'message': message}), 400)
