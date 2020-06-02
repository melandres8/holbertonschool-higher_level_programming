#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry():
    """ Defining methods and instances
    """
    def area(self):
        """ Area without implementation
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validating an integer
        """
        if type(value) != int:
            raise TypeError(str(name) + " must be an integer")
        elif value <= 0:
            raise ValueError(str(name) + " must be greater than 0")
