#!/usr/bin/python3
"""
    This module defines an add function
    and it's tested on /tests folder.

"""


def add_integer(a, b=98):
    """
    Adds a and b just if they're int or floats,
    """
    if not (isinstance(a, int) or isinstance(a, float)) or \
       not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
