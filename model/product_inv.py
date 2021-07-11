from sqlalchemy import Column, String, Integer, Float

from model.base import Base
from dataclasses import dataclass

@dataclass
class ProductInv(Base):
    __tablename__ = 'product_inventory'
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
