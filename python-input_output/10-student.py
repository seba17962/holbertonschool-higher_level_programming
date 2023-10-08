#!/usr/bin/python3
"""_summary_
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """_summary_

        Args:
            first_name (str):
            last_name (str:
            age (int):
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representing the Student instance.
        """
        if attrs is None:
            attrs = self.__dict__.keys()

        json_dict = {}

        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)

        return json_dict
