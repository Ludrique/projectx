from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:12345678#@localhost/postgres')
Session = sessionmaker(bind=engine)

Base = declarative_base()
