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
        return f"[Square] ({id}) {self.x}/{self.y} - {self.height}"
