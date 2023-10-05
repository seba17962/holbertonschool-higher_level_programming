#!/usr/bin/python3
"""_summary_
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """_summary_

    Args:
        BaseGeometry (_type_): _description_
    """
    def __init__(self, width, height):
        self.integer_validator("width", self.__width)
        self.__width = width
        self.integer_validator("height", self.__height)
        self.__height = height
