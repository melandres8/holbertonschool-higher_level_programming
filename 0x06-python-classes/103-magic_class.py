#!/usr/bin/python3
"""From bytecode to python code"""
import math


class MagicClass:
    """__init__ constructor"""
    def __init__(self, radius=0):
        """
        Args:
            radius (int): radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Returning the area of a circle"""
        return((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Returning the circumference of a circle"""
        return((2 * math.pi) * self.__radius)
