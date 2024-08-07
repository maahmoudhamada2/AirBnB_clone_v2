#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from user import User, Base

engine = create_engine("mysql+mysqldb://root:root@localhost/site")
Base.metadata.create_all(engine)

session_factory = sessionmaker(bind=engine)
self_session = scoped_session(session_factory)


u1 = User(name="Mahmoud", age=27)

self_session.add(u1)
self_session.commit()
