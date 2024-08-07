#!/usr/bin/python3
"""DBStorage class module"""

from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor method"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        dbUrl = "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db)
        self.__engine = create_engine(dbUrl, pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """Method to create both session and create tables in db"""
        from models.city import City
        from models.state import State

        Base.metadata.create_all(self.__engine)
        session_factory =\
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def new(self, obj):
        """Method to add object to db"""
        self.__session.add(obj)

    def save(self):
        """Method to commit records into db"""
        self.__session.commit()

    def delete(self, obj=None):

        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def all(self, cls=None):
        """Method to return list of all objs available"""
        from models.state import State
        from models.city import City
        if cls is None:
            custom_objs = {}
            records = []
            classes = [State, City]
            for cls in classes:
                records.append(self.__session.query(cls).all())

            for row in records:
                key = "{}.{}".format(row[0].__class__.__name__, row[0].id)
                custom_objs.update({key: row[0]})
            return custom_objs
        else:
            custom_objs = {}
            records = self.__session.query(cls).all()
            for obj in records:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                custom_objs.update({key: obj})
            return custom_objs
