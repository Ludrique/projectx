from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

#many to one relationship
class ContactDetails(Base):
    __tablename__ = 'contact_details'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String)
    address = String(String)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref="contact_details")

    def __repr__(self):
        

    def __init__(self, phone_number, address, actor):
        self.phone_number =phone_number
        self.address = address
        self.actorv = actor
