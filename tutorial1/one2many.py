from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine('postgresql://postgres:12345678#@localhost/postgres')

class Article(Base):
    __tablename__ = 'articles'
    id=Column(Integer, primary_key=True)
    comments=relationship("Comment")

class Comment(Base):
    __tablename__ = 'comments'
    id=Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))

#one to many, an instance of the article class could be associated with many instances of the comment class
