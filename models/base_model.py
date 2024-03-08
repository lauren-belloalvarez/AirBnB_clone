#!/usr/bin/python3

"""Base Module"""

import uuid
from datetime import datetime


class BaseModel:
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
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        :return: prints out a class name,
        followed by the id and a dictionary
        """
        holder = "[{}] ({}) {}"
        return holder.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Method to update the public instance attribute
        "updated_at"\
        With the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        :return: a dictionary containing all
        the key value pairs
        """
        class_name = self.__class__.__name__
        instance_dict = {key: value for key, value in vars(self).items()}
        instance_dict["__class__"] = class_name
        instance_dict["created_at"] = datetime.isoformat(self.created_at)
        instance_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return instance_dict
