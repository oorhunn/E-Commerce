from sqlalchemy import Column, String, Integer, Table, ForeignKey, Boolean
from model.base import Base
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref

@dataclass
class Users(Base):
    __tablename__ = 'users'
    user_id: int
    username: str
    email: str
    password: str
    register_date: str
    proved: bool

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    register_date = Column(String)
    proved = Column(Boolean)

    def __init__(self, username, email,password, register_date, proved):
        self.username = username
        self.password = password
        self.email = email
        self.register_date = register_date
        self.proved = proved
