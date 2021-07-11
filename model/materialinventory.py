from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from model.base import Base
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass

@dataclass
class MaterialInventory(Base):
    __tablename__ = 'material_inventory'
    material_id: int
    material_name: str
    warehouse_id: int
    material_quantity: str
    supplier_id: int

    material_id = Column(Integer, primary_key=True)
    material_name = Column(String)
    warehouse_id = Column(Integer, ForeignKey('warehouses.warehouse_id'))
    material_quantity = Column(String)
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'))
    ware = relationship('Warehouses', backref='material_inventory')
    supp = relationship('Suppliers', backref='material_inventory')

    def __init__(self, ware, supp, material_name, material_quantity):
        self.ware = ware
        self.supp = supp
        self.material_name = material_name
        self.material_quantity = material_quantity
