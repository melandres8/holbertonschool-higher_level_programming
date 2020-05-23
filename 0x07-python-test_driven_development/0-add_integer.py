#!/usr/bin/python3
"""
    Function to adds 2 integers.
    In this function we must
    adds two numbers and make a test.
"""


def add_integer(a, b=98):
    """
        Return the add of two integers
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
