#!/usr/bin/python3
"""Square class"""


class Square():

    """__init__ constructor: Runs always when we
    create a new instance of a class
    Attributes:
        attr1 (int): is the size of a square
    """
    def __init__(self, size=0):
        """
        Inicializing my class with

        Args:
            size (int): size of a square
        """
        self.__size = size

    @property
    def size(self):
        """Getter, retrieve the size of a square
        this methods is useful to handle with
        privacity of our instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Handle the value of a size if
        is an integer or not

        Args:
            size (int): size of a square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculating the area of a square"""
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """Printing a Square and validating
        if the size is 0 or not"""
        for row in range(self.__size):
            print('#' * self.__size)
        if self.__size == 0:
            print()
