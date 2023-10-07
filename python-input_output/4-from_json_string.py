#!/usr/bin/python3
"""_summary_
"""
import json


def from_json_string(my_str):
    """_summary_

    Args:
        my_str (_type_): _description_

    Returns:
        _type_: _description_
    """
    if my_str is not None and my_str:
        with open(my_str, "r", encoding="utf-8") as f:
            return json.load(f)
