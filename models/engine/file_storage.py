#!/usr/bin/python3

import os
import json
from models.base_model import BaseModel

"""
a class FileStorage that serializes
instances to a JSON file and deserializes
JSON file to instances
"""


class FileStorage:
    """
    class  that serializes instances to a Json
    file and deserializes Json file to instances
    """
    def __init__(self):
        self.__objects = {}
        self.__file_path = "file.json"

    def all(self):
        """
        All Objects
        return: dictionary __object
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj
        with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialization
        :return: nothing
        """
        with open(self.__file_path, 'w') as f:
            obj_dict = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(obj_dict, f, indent=4, sort_keys=True, default=str)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        all_classes = {
                "BaseModel": BaseModel
        }
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    name = key.split(".")[0]
                    if name in all_classes:
                        obj = all_classes[name](**value)
                        self.__objects[key] = obj
