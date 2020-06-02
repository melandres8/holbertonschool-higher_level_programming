#!/usr/bin/python3
"""Implementing the super() method and more inheritance"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class
    """
    def __init__(self, size):
        """Constructor method

            Args:
                size: square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)  # call init of rectangle class
        self.__size = size

    def __str__(self):
        """ Returning the string representation
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
