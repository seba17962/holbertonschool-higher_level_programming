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
        
        if all(isinstance(i, int) for i in self):
            print(sorted(self))
