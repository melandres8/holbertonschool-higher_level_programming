#!/usr/bin/python3
"""Setting an attribute"""


def add_attribute(obj, name, value):
    """ Function to adds attribute

        Args:
            obj: object
            name: attribute type
            value: Value to the attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
