from model.base import Session, engine, Base
from datetime import datetime
from model.users import Users
from model.products import Products
from model.warehouses import Warehouses


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
    anan = Products(**kwargs)
    session.add(anan)
    session.commit()
    session.close()

def inventorydelete(id):
    Base.metadata.create_all(engine)
    session = Session()
    temp = session.query(Products).get(id)
    session.delete(temp)
    session.commit()
    session.close()

def warehouserr():
    Base.metadata.create_all(engine)
    session = Session()
    temp = session.query(Warehouses).filter(Warehouses.warehouse_id==1).first()
    return temp


ses = Session()
warehouse = warehouserr()

body = {
    'product_name': 'name',
    'warehouse': warehouse,
    'size': 'size',
    'price': 12.2,
    'register_date': 'register_date',
    'photo_link': 'photo_link',
    'category': 'category',
    'product_quantity': 55
}

inventoryinserter(body)

