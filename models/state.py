#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
from models import storage
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade="all, delete")
    else:
        name = ""
        cities = ""

        @property
        def cities(self):
            """The cities getter method"""
            objs = storage.all(City)
            objs_list = []
            for obj in objs.values():
                if obj.state_id == self.id:
                    objs_list.append(obj)
            return objs_list
