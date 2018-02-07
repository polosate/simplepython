from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.exc import IntegrityError

from database import Base, db_session


class TTask(Base):
    """
    Tasks table
    """
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    name = Column(String(256))
    desc = Column(String(256))
    done = Column(Boolean, default=False)

    query = db_session.query_property()

    # def __init__(self, name, desc, user_id):
    #     self.name = name
    #     self.desc = desc
    #     self.user_id = user_id

    def __repr__(self):
        return '<id {}, name {}, desc {}, done {}>'\
            .format(self.task_id, self.name, self.desc, self.done)

    @classmethod
    def add_record(cls, name, desc, user_id):
        try:
            new_task = TTask(name=name, desc=desc,user_id=user_id)
            db_session.add(new_task)
            db_session.commit()
        except IntegrityError:
            return None
        return new_task.task_id


class TUser(Base):
    """
    Users table
    """
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(256))
    mid_name = Column(String(256))
    last_name = Column(String(256))
    birthday = Column(Date)

    query = db_session.query_property()

    # def __init__(self, first_name, last_name):
    #     self.first_name = first_name
    #     self.last_name = last_name

    def __repr__(self):
        return '<id {}, first_name {}, last_name {}>'\
            .format(self.task_id, self.first_name, self.last_name)

