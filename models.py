from database import Base, db_session
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.types import DateTime


class SignUps(Base):
    """
    Example SignUps table
    """
    __tablename__ = 'signups'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    email = Column(String(256), unique=True)
    date_signed_up = Column(DateTime())


class Task(Base):
    """
    Task table
    """
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    desc = Column(String(256))
    done = Column(Boolean, default=False)

    query = db_session.query_property()

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return '<id {}, name {}, desc {}, done {}>'.format(self.id, self.name, self.desc, self.done)
