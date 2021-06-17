from sqlalchemy import Column, String, Integer, Float
from model.base import Base

class Inventory(Base):
    __tablename__ = 'inventory'
#    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    category = Column(String)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    size = Column(String)
    register_date = Column(String)
    photo_link = Column(String)

    def __init__(self, category, name, quantity, price, size,register_date, photo_link):
        self.category = category
        self.name = name
        self.quantity = quantity
        self.price = price
        self.size = size
        self.register_date = register_date
        self.photo_link = photo_link