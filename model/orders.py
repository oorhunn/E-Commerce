from sqlalchemy import Column, String, Integer, Float, ForeignKey
from model.base import Base
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass


@dataclass
class Orders(Base):
    __tablename__ = 'orders'
    # product_name: str   #
    order_quantity: int
    order_date: str
    order_giver: str
    order_code: int
    total_price: int
    activeness: str
    cargo_number: str
    order_address: str
############################################################################
    order_code = Column(Integer, primary_key=True)
    # product_name = relationship(ForeignKey, 'products', back_populates='orders')    #
    order_quantity = Column(Integer)
    order_date = Column(Integer)
    order_giver = Column(String)
    total_price = Column(Float)
    activeness = Column(String)
    cargo_number = Column(String)
    order_address = Column(String)

    def __init__(self, order_quantity, order_date, order_giver, total_price, activeness, cargo_number, order_address):
        self.order_quantity = order_quantity
        self.order_date = order_date
        self.order_giver = order_giver
        # self.product_name = product_name
        self.total_price = total_price
        self.activeness = activeness
        self.cargo_number = cargo_number
        self.order_address = order_address
