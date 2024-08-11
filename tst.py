#!/usr/bin/python3

from models.city import City
from models.state import State
from models import storage


classes = [City, State]
custom_objs = {}
for cls in classes:
    records = storage._DBStorage__session().query(cls).all()
    for row in records:
        key = "{}.{}".format(row.__class__.__name__, row.id)
        custom_objs.update({key: row})

for values in custom_objs.values():
    print(values)
