#!/usr/bin/python3

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class User(Base):

    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    age = Column(Integer, nullable=False)


