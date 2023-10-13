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
        if list_dictionaries is not None and list_dictionaries:
            return json.dumps(list_dictionaries)
