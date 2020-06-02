#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defining constructor method
    """
    def __init__(self, width, height):
        """ Constructor

            Args:
                width: Rectangle width
                height: Rectangle height
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
