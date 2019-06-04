from flask import Flask
from flask_sqlalchemy import SQLAlchemy, create_engine

app = Flask(__name__)

engine = create_engine('postgresql://postgres:12345678#@localhost/postgres')

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    mobile_phone = relationship("MobilePhone", uselist=False, back_populates="person")

class MobilePhone(Base):
    __tablename__ = 'mobile_phones'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship("Person", back_populates="mobile_phone")

''' one to one, refers to relationships where an instance of a particular class may only be associated with one instance
 of another class.
 uselist=False, makes sqlalchemy understand that mobile_phone will hold only a single instance and not an array (multiple) of instances.
 back_populates instructs sqlalchemy to populate the other side of the mapping '''
