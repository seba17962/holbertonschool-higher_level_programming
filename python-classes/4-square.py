#!/usr/bin/python3
""" This module define a class Square """


class Square():
    """ This class define a Square """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    pass

    def area(self):
        return (self.__size ** 2)
