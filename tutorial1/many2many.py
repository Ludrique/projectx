from flask import Flask
from flask_sqlalchemy import SQLAlchemy, create_engine

app = Flask(__name__)

engine = create_engine('postgresql://postgres:12345678#@localhost/postgres')

students_classes_association = Table('students_classes', Base.metadata,
Column('student_id', Integer, ForeignKey('classes.id')),
Column('class_id', Integer, ForeignKey('classes.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    classes = relationship("Class", secondary=students_classes_association)

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)

''' many to many, when instances of another class can have zero or more associations to instances of another class.
   '''
