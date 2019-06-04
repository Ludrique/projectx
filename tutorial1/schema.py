from marshmallow import *

class AuthorSchema(ModelSchema):

    author = Author(name="Chuck Paluhniuk")
    session.add(author)
    session.commit()

    class Meta:
        model = Author
        dump_data = author.schema.dump(author).data
        print(dump_data)

class BookSchema(ModelSchema):
    class Meta:
        model = Book
        book = Book(title = "Fight Club", author=author)
        session.add(book)
        session.commit()
        load_data = author.schema.load(dump_data, session=session).data
        print(load_data)
        #optionally attach a session
        #to use for desiarilization
        sqla_session = session

author_schema = AuthorSchema()
