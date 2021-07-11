from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from model.base import Base
from sqlalchemy.orm import relationship, backref
from  dataclasses import dataclass

@dataclass
class Warehouses(Base):
    __tablename__ = 'warehouses'
    warehouse_id: int
    warehouse_name: str
    w_responsible: str

    warehouse_id = Column(Integer, primary_key=True)
    warehouse_name = Column(String)
    w_responsible = Column(String)

    def __init__(self, warehouse_name, w_responsible):
        self.warehouse_name = warehouse_name
        self.w_responsible = w_responsible


