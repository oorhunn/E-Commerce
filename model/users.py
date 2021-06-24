from sqlalchemy import Column, String, Integer
from model.base import Base
from dataclasses import dataclass

@dataclass
class Users(Base):
    __tablename__ = 'users'
    id: int
    username: str
    password: str
    register_date: str
    proved: str
#    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    register_date = Column(String)
    proved = Column(String)
    # orders = Column(String)

    def __init__(self, username, password, register_date, proved):
        self.username = username
        self.password = password
        self.register_date = register_date
        self.proved = proved