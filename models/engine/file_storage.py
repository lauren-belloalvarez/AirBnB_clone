#!/usr/bin/python3


from os import path
import json
from models.base_model import BaseModel

"""
a class FileStorage that serializes
instances to a JSON file and deserializes
JSON file to instances
"""


class FileStorage():
    """
    class  that serializes instances to a Json
    file and deserializes Json file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        :return: dictionary __object
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj
        with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialization
        :return: nothing
        """
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            serialized_objects = {}
            for key, obj in self.__objects.items():
                serialized_objects[key] = obj.to_dict()
            json.dump(serialized_objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
