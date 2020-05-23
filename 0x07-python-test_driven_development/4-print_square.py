#!/usr/bin/python3
"""
    print square function.
"""


def print_square(size):
    """
        This function print a square of '#'

        Args:
            size: (int) get the size of my square.
    """

    if (type(size) != int or type(size) is float or size is None):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for item in range(size):
        print("#" * size)
