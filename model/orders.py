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
    product_id: int
    cargo_number: str
    activeness: bool

    code = Column(Integer, primary_key=True)
    product = relationship('Products', backref='orders')
    user = relationship('Users', backref='orders')
    order_giver_id = Column(Integer, ForeignKey('users.user_id'))
    total_price = Column(Float)
    order_date = Column(String)
    order_quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    cargo_number = Column(String)
    activeness = Column(Boolean)

    def __init__(self, product, user, total_price, order_date, order_quantity, cargo_number, activeness):
        self.product = product
        self.user = user
        self.total_price = total_price
        self.order_date = order_date
        self.order_quantity = order_quantity
        self.cargo_number = cargo_number
        self.activeness = activeness

