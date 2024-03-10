#!/usr/bin/python3


from os import path
import json
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
    __object = {}

    def all(self):
        """
        :return: dictionary __object
        """
        return self.__object

    def new(self, obj):
        """
        sets in __objects the obj
        with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)

    def save(self):
        """
        Serialization
        :return: nothing
        """
        f = open(self.__file_path, 'w')
        json.dump(self.__object, f)
        f.close()

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
