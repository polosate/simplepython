from json import loads, JSONDecodeError

from flask import redirect, url_for, jsonify, request, make_response

from app import app
from app.middleware import task


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found',
                                  'message': error}),
                         404)


@app.errorhandler(400)
def json_parse_error():
    return make_response(jsonify({'error': 'Request is not valid'}), 400)


@app.route("/v1/tasks/<int:user_id>/")
def get_tasks(user_id):
    tasks = task.get_tasks(user_id)
    if not tasks:
        return not_found("Tasks for user_id {} not found".format(user_id))
    return jsonify([t.to_dict() for t in tasks])


@app.route("/v1/task/<int:task_id>/", methods=["GET"])
def get_task(task_id):
    t = task.get_task(task_id)
    if not task:
        return not_found("Task {} not found".format(task_id))
    return jsonify(t.to_dict())


@app.route("/v1/task/", methods=["POST"])
def create_task():
    try:
        r = loads(request.data)
        name = r["name"]
        desc = r["description"]
        user_id = r["user_id"]
    except (JSONDecodeError, KeyError):
        return json_parse_error()

    response = task.create_task(name, desc, user_id)
    if isinstance(response, str):
        return not_found(response)
    return redirect(url_for('get_task', task_id=response))

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

