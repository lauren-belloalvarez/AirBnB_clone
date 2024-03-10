#!/usr/bin/python3
"""
The FileStorage Module
"""
import os
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

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
        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}

        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            self.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
