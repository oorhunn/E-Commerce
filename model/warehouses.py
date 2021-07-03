from sqlalchemy import Column, String, Integer, Table, ForeignKey
from model.base import Base
from dataclasses import dataclass
from sqlalchemy.orm import relationship


@dataclass
class Warehouses(Base):
    __tablename__ = 'warehouses'
    warehouse_id: int
    warehouse_name: str
    wr_resp_person: str
############################################################################
    warehouse_id = Column(Integer, primary_key=True)
    warehouse_name = Column(String)
    wr_resp_person = Column(String)

    def __init__(self, warehouse_name, wr_resp_person):
        self.warehouse_name = warehouse_name
        self.wr_resp_person = wr_resp_person
