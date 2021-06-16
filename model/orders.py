from sqlalchemy import Column, String, Integer, Float
from model.base import Base

class Orders(Base):
    __tablename__ = 'orders'
#    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    product = Column(String)
    quantity = Column(String)
    total_price = Column(Float)
    activeness = Column(String)
    date = Column(String)
    cargo_number = Column(String)

    def __init__(self, product, quantity, total_price, activeness, date, cargo_number):
        self.product = product
        self.quantity = quantity
        self.total_price = total_price
        self.activeness = activeness
        self.date = date
        self.cargo_number = cargo_number
