from sqlalchemy import Column, String, Integer, Table, ForeignKey
from model.base import Base
from dataclasses import dataclass
from sqlalchemy.orm import relationship


@dataclass
class MaterialInventory(Base):
    __tablename__ = 'materialinventory'
    material_id: int
    material_name: str
    order_code: int
    warehouse_id: id
    material_quantity: int
    supplier_id: int

    material_id = Column(Integer, primary_key=True)
    material_name = Column(String)
    order_code = Column(Integer)
    warehouse_id = Column(Integer)
    material_quantity = Column(Integer)
    supplier_id = Column(Integer)
############################################################################
    def __init__(self, material_name, order_code, warehouse_id, material_quantity, supplier_id):
        self.material_name = material_name
        self.order_code = order_code
        self.warehouse_id = warehouse_id
        self.material_quantity = material_quantity
        self.supplier_id = supplier_id