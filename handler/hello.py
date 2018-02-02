from app import app


@app.route("/")
def hello():
    return "Hello Flask!"


@app.route("/<user_path>/")
def goodbye(user_path):
    return "The path is  %s" % user_path
