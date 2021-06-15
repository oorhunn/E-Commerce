from sqlalchemy import Column, String, Integer
from model.base import Base

class Products(Base):
    __tablename__ = 'products'
#    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    productname = Column(String)
    productcount = Column(Integer)
    productprice = Column(Integer)
    productsize = Column(String)
    # i left here
    register_date = Column(String)

    def __init__(self, username, password, register_date):
        self.username = username
        self.password = password
        self.register_date = register_date