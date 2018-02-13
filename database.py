from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# user = os.environ['POSTGRES_USER']
# pwd = os.environ['POSTGRES_PASSWORD']
# db = os.environ['POSTGRES_DB']
user = 'postgres'
pwd = 'postgres'
db = 'simplepython_db_1'
host = 'localhost'
port = '54321'
engine = create_engine('postgres://%s:%s@%s:%s/%s' % (user, pwd, host, port, db))

user_test = 'test'
pwd_test = 'test'
db_test = 'test_db_1'
host_test = 'localhost'
port_test = '54322'
test_engine = create_engine('postgres://%s:%s@%s:%s/%s' % (user_test, pwd_test, host_test, port_test, db_test))

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)


def init_test_db():
    import models
    Base.metadata.create_all(bind=test_engine)
