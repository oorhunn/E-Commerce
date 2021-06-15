import datetime

from model.users import Users
from model.base import Session, engine, Base
from datetime import datetime

def inster(kwargs):
    Base.metadata.create_all(engine)
    session = Session()
    abb = Users(**kwargs)
    session.add(abb)
    session.commit()
    session.close()
def dbsession():
    session = Session()
    return session


