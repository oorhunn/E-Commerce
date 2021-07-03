import model
import json
from model.users import Users
from model.base import Session, engine, Base
from datetime import datetime
from model.inventory import Inventory
from model.orders import Orders
from model.products import Products

date = datetime.utcnow()

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

def inventorydelete(id):
    Base.metadata.create_all(engine)
    session = Session()
    temp = session.query(Inventory).get(id)
    session.delete(temp)
    session.commit()


Base.metadata.create_all(engine)
session = Session()

anan = Orders(5 , date, 'mustaf', 64, 't', '123sdaf', 'asdfzxvc',)

session.add(anan)
session.commit()
session.close()

