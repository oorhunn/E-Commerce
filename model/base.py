from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:aaaaa@localhost:5432/duruh')
Session = sessionmaker(bind=engine)

Base = declarative_base()
