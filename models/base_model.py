#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
import models
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def date_converter(self, flag, key="", value=""):
        """Method to convert date from to isoformat"""
        if flag == 1:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            setattr(self, key, datetime.fromisoformat(value))

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        if not kwargs:
            self.id = str(uuid4())
            self.date_converter(1)

        else:
            self.id = str(uuid4())
            self.date_converter(1)
            for key in kwargs.keys():
                if key == '__class__':
                    continue
                elif key == 'updated_at' or key == 'created_at':
                    self.date_converter(2, key, kwargs[key])
                else:
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        custom_dict = self.__dict__.copy()
        if custom_dict.get('_sa_instance_state') is not None:
            custom_dict.pop('_sa_instance_state')
        return '[{}] ({}) {}'.format(cls, self.id, custom_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary.get('_sa_instance_state') is not None:
            dictionary.pop("_sa_instance_state")
        return dictionary

    def delete(self):
        """Method to delete an instance"""
        models.storage.delete(self)
