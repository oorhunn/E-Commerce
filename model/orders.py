from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from model.base import Base
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass


@dataclass
class Orders(Base):
    __tablename__ = 'orders'
    code: int
    order_giver_id: int
    total_price: float
    order_date: str
    order_quantity: int
    product_name: str

    code = Column(Integer, primary_key=True)
    order_giver_id = Column(Integer, ForeignKey('users.user_id'))
    total_price = Column(Float)
    order_date = Column(String)
    order_quantity = Column(Integer)
    product_name = Column(String, ForeignKey('products.product_name'))
    user = relationship('Users', backref='orders')

    def __init__(self, user, total_price, order_date, order_quantity, product_name):
        self.user = user
        self.total_price = total_price
        self.order_date = order_date
        self.order_quantity = order_quantity
        self.product_name = product_name

