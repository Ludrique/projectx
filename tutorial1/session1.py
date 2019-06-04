from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:12345678#@localhost/postgres')

#create a configured session class
session = sessionmaker(bind=engine)

#create a session
session = Session()
