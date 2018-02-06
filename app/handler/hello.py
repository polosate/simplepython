import datetime
from app import app
from models import SignUps
from database import db_session


@app.route("/hello")
def hello():
    signup = SignUps(name="John Doe", email="jd1@example.com", date_signed_up=datetime.datetime.now())
    db_session.add(signup)
    db_session.commit()
    return "Success!"


@app.route("/user/get/")
def goodbye():
    return "User: "
