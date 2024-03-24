#!/usr/bin/python3

"""Base Module"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """
    a class BaseModel that defines all
    common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        :param kwargs: holds all pass argument strings.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.engine.storage.new(self)

    def __str__(self):
        """
        :return: string representation of the
        instance
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__)

    def save(self):
        """
        Method to update the public instance attribute
        "updated_at" with the current datetime
        """
        self.updated_at = datetime.now()
        models.engine.storage.save()

    def to_dict(self):
        """
        :return: a dictionary containing all
        the key value pairs
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
