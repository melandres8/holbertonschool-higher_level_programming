#!/usr/bin/python3
"""Function that returns if instance of or if
the object is an instance of a class that
inherited from specified class otherwise False"""


def is_kind_of_class(obj, a_class):
    """ Verifying if is same class or inherit from
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
