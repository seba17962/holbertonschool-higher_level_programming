#!/usr/bin/python3
"""_summary_

Raises:
    TypeError: _description_
    ValueError: _description_
    TypeError: _description_
    ValueError: _description_

Returns:
    _type_: _description_
"""


class Rectangle:
    """_summary_
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0

        return (self.__height + self.__width) * 2

    def __str__(self):
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result

        for i in range(self.__height):
            for _ in range(self.__width):
                result += str(self.print_symbol)
            if (i != self.__height - 1):
                result += "\n"
        return result

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
