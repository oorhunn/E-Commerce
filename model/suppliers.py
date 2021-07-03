from sqlalchemy import Column, String, Integer, Table, ForeignKey
from model.base import Base
from dataclasses import dataclass
from sqlalchemy.orm import relationship


@dataclass
class Suppliers(Base):
    __tablename__ = 'suppliers'
    supplier_id: int
    supplier_name: str
    supplier_phone: str
    supplier_reponsible: str
    contract_date: str
    mail: str
############################################################################
    supplier_id = Column(Integer, primary_key=True)
    supplier_name = Column(String)
    supplier_phone = Column(String)
    supplier_reponsible = Column(String)
    contract_date = Column(String)
    mail = Column(String)

    def __init__(self, supplier_name, supplier_phone, supplier_reponsible, contract_date, mail):
        self.supplier_name = supplier_name
        self.supplier_phone = supplier_phone
        self.supplier_reponsible = supplier_reponsible
        self.contract_date = contract_date
        self.mail = mail