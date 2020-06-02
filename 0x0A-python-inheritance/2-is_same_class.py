#!/usr/bin/python3
"""Function that return if an object
is an instance of a class or not"""


def is_same_class(obj, a_class):
    """ Verifying if is the same object
    """
    if type(obj) == a_class:
        return True
    else:
        False
