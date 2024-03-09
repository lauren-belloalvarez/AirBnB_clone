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

    __file_path = "file.json"
    __object = {}

    def all(self):
        """
        :return: dictionary __object
        """
        return  FileStorage.__object

    def new(self, obj):
        key = "{}.{}".format(type(type(obj).__name__, obj.id)

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
            with open(Self.__file_path, 'r'):
                self.__object = json.load(self.__file_path)
        else:
            pass
