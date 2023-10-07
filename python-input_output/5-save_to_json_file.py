#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj (list): obj
        filename (str): json representation
    """
    if filename is not None and filename:
        with open(filename, 'w', encoding="utf-8") as f:
            x = json.dump(my_obj, f)
