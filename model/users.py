from sqlalchemy import Column, String, Integer, Date
from model.base import Base

class Users(Base):
    __tablename__ = 'users'
#    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    register_date = Column(Date)

    def __init__(self, username, password, register_date):
        self.username = username
        self.password = password
        self.register_date = register_date