from flask import Flask
from flask_sqlalchemy import SQLAlchemy, create_engine

app = Flask(__name__)

engine = create_engine('postgresql://postgres:12345678#@localhost/postgres')

class Tyre(Base):
    __tablename__ = 'tyres'
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship("Car")

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)

#similar to one to many, lets say we want to map the relationship between instances of Tyre to an instance of a car
