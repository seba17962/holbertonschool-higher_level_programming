#!/usr/bin/python3
"""_summary_
"""
from models.base import Base


class Rectangle(Base):
    """_summary_

    Args:
        Base (class): case base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return (self.__width * self.__height)

    def display(self):
        """_summary_
        """
        for _ in range(self.y):
            print()
        for _ in range(self.__height):
            print(' ' * self.x + "#" * self.__width, end='')
            print()

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """_summary_
        """
        if args and len(args) > 0:

            opt_args = ["id", "width", "height", "x", "y"]

            for count, arg in enumerate(args):
                setattr(self, opt_args[count], arg)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """_summary_
        """
        representation = {
            'id' : self.id,
            'width' : self.width,
            'height' : self.height,
            'x' : self.x,
            'y': self.y
        }
        return representation
