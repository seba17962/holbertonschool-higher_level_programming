#!/usr/bin/python3
def inherits_from(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return type(obj) is not a_class
