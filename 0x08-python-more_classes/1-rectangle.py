#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle():
    """
        Contructor method
        Attributes:
            attr1: (int) Rectangle width
            attr2: (int) Rectangle height
    """
    def __init__(self, width=0, height=0):
        """
            Instance attributes
            Args:
                width: (int) Rectangle width
                height: (int) Rectangle height
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Getter, retrieve the width of a rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
