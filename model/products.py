from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from model.base import Base
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref


@dataclass
class Products(Base):
    __tablename__ = 'products'

    product_id: int
    category: str
    product_quantity: int
    product_name: str
    size: str
    price: float
    register_date: str
    photo_link: str

    product_id = Column(Integer, primary_key=True)
    category = Column(String)
    product_quantity = Column(Integer)
    product_name = Column(String)
    size = Column(String)
    price = Column(Float)
    register_date = Column(String)
    photo_link = Column(String, nullable=True)
    warehouse_id = Column(Integer, ForeignKey('warehouses.warehouse_id'), nullable=True)
    warehouse = relationship('Warehouses', backref='products')

    def __init__(self, product_name, size, price, register_date, photo_link, category, product_quantity, warehouse_id):
        self.product_name = product_name
        self.warehouse_id = warehouse_id
        self.size = size
        self.price = price
        self.register_date = register_date
        self.photo_link = photo_link
        self.category = category
        self.product_quantity = product_quantity

    def update(self, kwargs):
        print('product update is alive')
        for key in kwargs:
            value = kwargs[key]
            if hasattr(self, key) and not isinstance(value, list):
                setattr(self, key, value)
    def columns_to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_