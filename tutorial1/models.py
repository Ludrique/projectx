import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

engine = sa.create_engine('postgresql://postgres:12345678#@localhost/postgres')
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)

    def __repr__(self):
        return "<Author(name={self.name!r})>".format(self=self)

class Book(Base):
    __tablename__ = 'books'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    author_id = sa.Column(sa.Integer, sa.ForeignKey("authors.id"))
    author = relationship("Author", backref=backref("books"))

Base.metadata.create_all(engine)
