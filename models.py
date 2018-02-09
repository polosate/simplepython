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

    @classmethod
    def add_record(cls, name, desc, user_id):
        try:
            new_task = TTask(name=name, desc=desc, user_id=user_id)
            db_session.add(new_task)
            db_session.commit()
        except IntegrityError:
            return None
        return new_task.task_id

    @classmethod
    def get_records(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()


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

    @classmethod
    def add_record(cls, **kwargs):
        try:
            new_user = TUser()
            db_session.add(new_user)
            db_session.commit()
        except IntegrityError:
            return None
        return new_user.user_id
