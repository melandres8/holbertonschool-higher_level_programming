#!/usr/bin/python3
""" Applying inheritance and super() method
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Constructor method

            Args:
                size: square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)  # call init of rectangle class
        self.__size = size
