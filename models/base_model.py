#!/usr/bin/python3

"""Base Module"""


import uuid
from models import storage
from datetime import datetime


class BaseModel():
    """
    a class BaseModel that defines all
    common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        :param kwargs: holds all pass argument strings.
        """

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)
                    return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        storage.new(self)

    def __str__(self):
        """
        :return: string representation of the
        instance
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Method to update the public instance attribute
        "updated_at"\
                With the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        :return: a dictionary containing all
        the key value pairs
        """
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict
