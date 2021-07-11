from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from model.base import Base
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass

@dataclass
class Suppliers(Base):
    __tablename__ = 'suppliers'
    supplier_id: int
    supplier_name: str
    supplier_responsible: str
    mail: str
    supplier_phone: str
    contract_date: str

    supplier_id = Column(Integer, primary_key=True)
    supplier_name = Column(String)
    supplier_responsible = Column(String)
    mail = Column(String)
    supplier_phone = Column(String)
    contract_date = Column(String)

    def __init__(self, supplier_name, supplier_responsible, mail, supplier_phone, contract_date):
        self.supplier_name = supplier_name
        self.supplier_responsible = supplier_responsible
        self.mail = mail
        self.supplier_phone = supplier_phone
        self.contract_date = contract_date


