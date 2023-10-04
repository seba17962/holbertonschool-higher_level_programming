#!/usr/bin/python3
"""_summary_
"""
class MyList(list):
    """_summary_

    Args:
        list (_type_): _description_
    """
    def print_sorted(self):
        """_summary_
        """
        if isinstance(self, int):
            print(sorted(self))
