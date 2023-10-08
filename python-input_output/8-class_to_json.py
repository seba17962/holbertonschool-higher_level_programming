#!/usr/bin/python3
"""returns the dictionary description with simple data structure
"""
def class_to_json(obj):
    """
    Converts an object of a class into a dictionary for JSON serialization.

    Args:
        obj: An object of a class.

    Returns:
        dict: A dictionary representing the object in JSON-compatible format.
    """
    # Get the dictionary of attributes from the object
    obj_dict = obj.__dict__
    
    # Create a new dictionary to store serializable attributes
    json_dict = {}
    
    # Filter serializable attributes (lists, dictionaries, strings, integers, and booleans)
    for key, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    
    return json_dict

