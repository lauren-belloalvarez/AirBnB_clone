#!/usr/bin/python3


import json
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

    def __int__(self):
        self.__file_path = "file.json"
        self.__object = {}

    def all(self):
        """
        :return: dictionary __object
        """
        return self.__object

    def new(self, obj):
        key = f"{obj.__class__.__name__}#{obj.id}"
        self.__object[key] = obj

    def save(self):
        """
        Serialization
        :return: nothing
        """
        with open(self.__file_path, 'w') as file:
            json.dump(self.__object, file)

    def reload(self):
        """
        Deserialization
        :return:
        """
        if self.__file_path:
            f = json.load(self.__file_path)
            self.__object = f
        else:
            pass
