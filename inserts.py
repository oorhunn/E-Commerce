from model.product import Product
from model.users import Users

from model.base import Session, engine, Base
from datetime import date

def inst(username, password):
    Base.metadata.create_all(engine)
    session = Session()
    abb = Users(username, password, date.today())
    session.add(abb)
    session.commit()
    session.close()

