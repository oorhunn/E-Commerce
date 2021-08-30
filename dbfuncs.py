from model.base import Session, engine, Base
from datetime import datetime
from model.users import Users
from model.products import Products
from model.warehouses import Warehouses
from model.orders import Orders

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


def add_order(proid, userid):
    Base.metadata.create_all(engine)
    session = Session()
    pro = session.query(Products).filter(Products.product_id == proid).first()
    user = session.query(Users).filter(Users.user_id == userid).first()
    anan = Orders(pro, user, 50, date, 50, 'anan', True)
    session.add(anan)
    session.commit()
    session.close()


def delete_order(order_id):
    Base.metadata.create_all(engine)
    session = Session()
    temp = session.query(Orders).get(order_id)
    session.delete(temp)
    session.commit()
    session.close()


def inventoryinserter(kwargs):
    Base.metadata.create_all(engine)
    session = Session()
    abb = Products(**kwargs)
    session.add(abb)
    session.commit()
    session.close()

def product_id_founder():
    Base.metadata.create_all(engine)
    session = Session()
    temp = session.query(Products).all()
    i = 0
    highest = 0
    while i < len(temp):
        compared = temp[i].product_id
        if compared > highest:
            highest = compared
        i = i + 1
    return highest
