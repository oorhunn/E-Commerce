from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from model.base import Base
from dataclasses import dataclass

@dataclass
class Products(Base):
    __tablename__ = 'products'
    product_name: str
    size: str
    price: float
    register_date: str
    photo_link: str

    product_name = Column(String, primary_key=True)
    size = Column(String)
    price = Column(Float)
    register_date = Column(String)
    photo_link = Column(String)

    def __init__(self, product_name, size, price, register_date, photo_link):
        self.product_name = product_name
        self.size = size
        self.price = price
        self.register_date = register_date
        self.photo_link = photo_link