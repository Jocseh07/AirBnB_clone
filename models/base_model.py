#!/usr/bin/python3
"""Defines all common attributes/methods for other classes."""

from datetime import datetime
from uuid import uuid4

import models


class BaseModel:
    """Represent BaseModel of the project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
          *args (any): unused.
          **kwargs (dict): key/valueparse pairs
        """

        form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, form)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return dictionary containing all key/values of __dict__."""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict

    def __str__(self):
        """Return string representation of BaseModel."""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
