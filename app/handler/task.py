from json import loads, JSONDecodeError

from flask import redirect, url_for, jsonify, request, make_response

from app import app
from app.middleware import task


@app.errorhandler(404)
def not_found(task_id):
    return make_response(jsonify({'error': 'Task {} not found'.format(task_id)}), 404)


@app.errorhandler(400)
def json_parse_error():
    return make_response(jsonify({'error': 'Request is not valid'}), 400)


@app.route("/v1/tasks/")
def get_tasks():
    tasks = task.get_task()
    return jsonify([t.to_dict() for t in tasks])


@app.route("/v1/task/<int:task_id>", methods=["GET"])
def get_task(task_id):
    t = task.get_task(task_id=task_id)
    if task is None:
        return not_found(task_id)
    return jsonify(t.to_dict())


@app.route("/v1/task/", methods=["POST"])
def create_task():
    try:
        r = loads(request.data)
        name = r["name"]
        desc = r["description"]
    except (JSONDecodeError, KeyError):
        return json_parse_error()

    task_id = task.create_task(name, desc)
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
#

