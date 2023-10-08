#!/usr/bin/python3
"""_summary_
"""


class Studend:
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representing the Student instance.
        """
        json_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return json_dict
