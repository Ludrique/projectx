from flask import Flask
from flask_sqlalchemy import SQLAlchemy, create_engine

app = Flask(__name__)

engine = create_engine('postgresql://postgres:12345678#@localhost/postgres')

class Product(Base):
    __tablename__ = 'products'
    id=Column(Integer, primary_key=True)
    title=Column('title', String(32))
    in_stock=Column('in_stock', Boolean)
    quantity=Column('quantity', Integer)
    price=Column('price', Numeric)
