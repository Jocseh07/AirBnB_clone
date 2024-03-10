#!/usr/bin/python3
"""Define file storage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent storage engine."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objecs the obj with key .id."""
        oname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(oname, obj.id)] = obj

    def save(self):
        """Serializes __objects to JSON file."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}

        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        "Deserialize the JSON file to __objects."
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(name)(**obj))
        except FileNotFoundError:
            return
