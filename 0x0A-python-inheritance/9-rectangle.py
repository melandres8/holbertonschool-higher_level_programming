#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defining constructor method
    """
    def __init__(self, width, height):
        """ Constructor method
            Args:
                width: rectangle width
                height: rectangle height
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Implementation of area
        """
        return self.__height * self.__width

    def __str__(self):
        """ String representation
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
