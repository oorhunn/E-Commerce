from sqlalchemy import Column, String, Integer, Float

from model.base import Base
from dataclasses import dataclass

@dataclass
class Inventory(Base):
    product_id: int
    product_name: str
    product_quantity: int
    category: str
    warehouse_id: int

    __tablename__ = 'inventory'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    product_quantity = Column(Integer)
    category = Column(String)
    warehouse_id = Column(Integer)

    def __init__(self, product_name, product_quantity, category, warehouse_id):
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.category = category
        self.warehouse_id = warehouse_id

    def update(self, kwargs):
        print('update is alive')
        for key in kwargs:
            value = kwargs[key]
            if hasattr(self, key) and not isinstance(value, list):
                setattr(self, key, value)
    def columns_to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_
