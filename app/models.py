from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text #
from sqlalchemy.sql.expression import null
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts" #this defines/intantiates a table

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=False) 
    owner = relationship("User") #Relationship will fetch data for us.

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer,ForeignKey("users.id",ondelete='CASCADE'),primary_key=True,nullable=False)
    post_id = Column(Integer,ForeignKey("posts.id",ondelete='CASCADE'),primary_key=True,nullable=False)

class Employer(Base):
    __tablename__ = 'employers'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    employee_count = Column(Integer, nullable=False, server_default='0')
    bed_count = Column(Integer, nullable=False, server_default='0')
    cell_phone = Column(String, nullable=True)
    address = Column(String, nullable=False)

