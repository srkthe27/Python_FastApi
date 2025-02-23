from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import base

class Blog(base):
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    body = Column(String)
    email = Column(String,ForeignKey('users.email'))
    creator = relationship("User",back_populates="blogs")
    __tablename__='blogs'

class User(base):
    __tablename__='users'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    email = Column(String,unique=True,index=True,nullable=False)
    password = Column(String,nullable=False)
    blogs = relationship("Blog",back_populates="creator")