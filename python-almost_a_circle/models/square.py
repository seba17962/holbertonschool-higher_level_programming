#!/usr/bin/python3
"""_summary_
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """_summary_
        """
        return self.width

    @size.setter
    def size(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """_summary_
        """
        if args and len(args) > 0:

            opt_args = ["id", "size", "x", "y"]

            for count, arg in enumerate(args):
                setattr(self, opt_args[count], arg)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
