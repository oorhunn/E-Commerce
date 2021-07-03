from sqlalchemy import Column, String, Integer, Table, ForeignKey
from model.base import Base
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref

@dataclass
class Users(Base):
    __tablename__ = 'users'
    user_id: int
    username: str
    password: str
    register_date: str
    proved: str
    ############################################################################
    #    __table_args__ = {'extend_existing': True}
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    register_date = Column(String)
    proved = Column(String)
    order_code = relationship('orders', ForeignKey)

    def __init__(self, username, password, register_date, proved, order_code):
        self.username = username
        self.password = password
        self.register_date = register_date
        self.proved = proved
        self.order_code = order_code
