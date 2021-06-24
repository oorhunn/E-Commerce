import model
import json
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

def inventorydelete(id):
    Base.metadata.create_all(engine)
    session = Session()
    temp = session.query(Inventory).get(id)
    session.delete(temp)
    session.commit()

date = datetime.utcnow()
body = {
    'category': 'Tulum',
    'name': 'isci tulumu',
    'quantity': 5,
    'price': 14.5,
    'size': 'M',
    'register_date': date,
    'photo_link': 'asdfghjkl'
}
inventoryinserter(body)