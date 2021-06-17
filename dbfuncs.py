import datetime

from model.users import Users
from model.base import Session, engine, Base
from datetime import datetime
from model.inventory import Inventory

def userinserter(kwargs):
    Base.metadata.create_all(engine)
    session = Session()
    abb = Users(**kwargs)
    session.add(abb)
    session.commit()
    session.close()
def dbsession():
    session = Session()
    return session

def inventoryinserter(kwargs):

    Base.metadata.create_all(engine)
    session = Session()
    anan = Inventory(**kwargs)
    session.add(anan)
    session.commit()
    session.close()

# Base.metadata.create_all(engine)
# session = Session()
# anan = session.query(Inventory).all()
# for a in anan:
#     print(a.name)
# condname = session.query(Users).filter(Users.username == 'mustaf').first()
# print(condname.username)


