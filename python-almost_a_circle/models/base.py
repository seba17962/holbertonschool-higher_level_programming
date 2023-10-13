#!/usr/bin/python3
"""_summary_
"""
import json


class Base:
    """_summary_
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """_summary_

        Args:
            list_dictionaries (_type_): _description_

        Returns:
            _type_: _description_
        """
        if list_dictionaries is not None and list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """_summary_

        Args:
            list_objs (_type_): _description_
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__

        jsn_d = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        filename = class_name + ".json"
        with open(filename, "w") as file:
            file.write(jsn_d)

    @staticmethod
    def from_json_string(json_string):
        if json_string is not None and json_string:
            return json.load(json_string)
        else:
            return "[]"
