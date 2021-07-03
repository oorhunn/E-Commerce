from sqlalchemy import Column, String, Integer, Table, ForeignKey, Float
from model.base import Base
from dataclasses import dataclass
from sqlalchemy.orm import relationship

@dataclass
class Products(Base):
    __tablename__ = 'products'
    product_name: str
    size: str
    price: float
    registered_date: str
    photo_link: str

    product_name = Column(String, primary_key=True)
    size = Column(String)
    price = Column(Float)
    registered_date = Column(String)
    photo_link = Column(String)

    def __init__(self, product_name, size, price, registered_date, photo_link):
        self.product_name = product_name
        self.size = size
        self.price = price
        self.registered_date = registered_date
        self.photo_link = photo_link