#!/usr/bin/python3

"""Base Module"""

import uuid
from datetime import datetime

import models


class BaseModel:
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = BaseModel.created_at
            self.updated_at = BaseModel.updated_at
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Method to update the public instance attribute "updated_at"\
            With the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Method to generate a dictionary representation\
            of the instance BaseModel"""
        class_name = self.__class__.__name__
        instance_dict = {key: value for key, value in vars(self).items()}
        instance_dict["__class__"] = class_name
        instance_dict["created_at"] = datetime.isoformat(self.created_at)
        instance_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return instance_dict

