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
        __cities = "list of cities instances"

        # TODO ADDING GETTER METHOD FOR CITY Class
        @property
        def cities(self):
            """The cities property."""
            objs = storage.all(City)
            print(self.id)
            print(objs)
            return self.__cities
