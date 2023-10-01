#!/usr/bin/python3
"""
    Module that contains the print_square function
    and it's tested on 4-print_square.txt

"""


def print_square(size):
    """Function that print a Square using #"""

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end='')
        print()
