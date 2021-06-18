import datetime

from model.users import Users
from model.base import Session, engine, Base
from datetime import datetime
from model.inventory import Inventory
from sqlalchemy import update

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

def _update_inventory_name(id, name):
    Base.metadata.create_all(engine)
    session = Session()
    session.query(Inventory).filter(Inventory.id==id).update({Inventory.name:name}, synchronize_session = False)
    session.commit()
    session.close()

def _update_inventory_category(id, category):
    Base.metadata.create_all(engine)
    session = Session()
    session.query(Inventory).filter(Inventory.id==id).update({Inventory.category:category}, synchronize_session = False)
    session.commit()
    session.close()

def _update_inventory_quantity(id, quantity):
    Base.metadata.create_all(engine)
    session = Session()
    session.query(Inventory).filter(Inventory.id==id).update({Inventory.quantity:quantity}, synchronize_session = False)
    session.commit()
    session.close()

def _update_inventory_price(id, price):
    Base.metadata.create_all(engine)
    session = Session()
    session.query(Inventory).filter(Inventory.id==id).update({Inventory.price:price}, synchronize_session = False)
    session.commit()
    session.close()

def _update_inventory_size(id, size):
    Base.metadata.create_all(engine)
    session = Session()
    session.query(Inventory).filter(Inventory.id==id).update({Inventory.size:size}, synchronize_session = False)
    session.commit()
    session.close()

def _update_inventory_photo_link(id, photo_link):
    Base.metadata.create_all(engine)
    session = Session()
    session.query(Inventory).filter(Inventory.id==id).update({Inventory.photo_link:photo_link}, synchronize_session = False)
    session.commit()
    session.close()