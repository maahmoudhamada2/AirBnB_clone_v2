#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from user import User, Base
from os import getenv
from models.state import State
from models.state import City


user = getenv("HBNB_MYSQL_USER")
pwd = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
db = getenv("HBNB_MYSQL_DB")
dbUrl = "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db)

engine = create_engine(dbUrl, pool_pre_ping=True)

sessino_factory = sessionmaker(bind=engine)
self_session = scoped_session(sessino_factory)

classes = [State, City]

records = []
for cls in classes:
    records.append(self_session.query(cls).all())

    
custom_objs = {}
for row in records:
    key = "{}.{}".format(row[0].__class__.__name__, row[0].id)
    print(key)
    custom_objs.update({key: row[0]})


print(custom_objs)
