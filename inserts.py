from model.product import Product
from model.users import Users

from model.base import Session, engine, Base
from datetime import date

Base.metadata.create_all(engine)
session = Session()
abb = Users('anilllll', 'asdfasdf', date.today())
session.add(abb)
session.commit()
session.close()

