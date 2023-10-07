#!/usr/bin/python3
"""creates an Object from a “JSON file”

Returns:
    obj:
"""
import json


def load_from_json_file(filename):
    """_summary_

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    if filename is not None and filename:
        with open(filename, 'r', encoding="utf-8") as f:
            return json.load(f)
