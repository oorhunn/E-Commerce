from model.base import Session, engine, Base
from datetime import datetime
from model.users import Users
from model.orders import Orders
from model.products import Products
# from model.inventory import Inventory

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

# def inventoryinserter(kwargs):
#     Base.metadata.create_all(engine)
#     session = Session()
#     anan = Inventory(**kwargs)
#     session.add(anan)
#     session.commit()
#     session.close()
#
# def inventorydelete(id):
#     Base.metadata.create_all(engine)
#     session = Session()
#     temp = session.query(Inventory).get(id)
#     session.delete(temp)
#     session.commit()

# Base.metadata.create_all(engine)
# session = Session()
# # temp = session.query(Users).filter(Users.user_id==1).first()
# # print(temp.username)
# # firstor = Orders(temp, 5.0, date, 50, 'yarak')
# pro = Products('ayakkabi', '45', 50.0, date, 'ananbaban')
# session.add(pro)
# session.commit()
# session.close()
