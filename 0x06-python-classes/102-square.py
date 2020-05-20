#!/usr/bin/python3
"""Square class"""


class Square():

    """Constructor function defined using
    __init__
    Attributes:
        attr1 (int): size if a main attr of a square
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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self, other):
        """Calculating the area of a square
        Return: True or False
        """
        return int(self.__size) * int(self.__size)

    def __lt__(self, other):
        """Calculating the area of a square
        Return: True or False
        """
        return self.size ** 2 < other.size ** 2

    def __le__(self, other):
        """Calculating the area of a square
        Return: True or False
        """
        return self.size ** 2 <= other.size ** 2

    def __eq__(self, other):
        """Calculating the area of a square
        Return: True or False
        """
        return self.size ** 2 == other.size ** 2

    def __ne__(self, other):
        """Calculating the area of a square
        Return: True or False
        """
        return self.size ** 2 != other.size ** 2

    def __gt__(self, other):
        """Calculating the area of a square
        Return: True or False
        """
        return self.size ** 2 > other.size ** 2

    def __ge__(self, other):
        """Calculating the area of a square
        Return: True or False
        """
        return self.size ** 2 >= other.size ** 2
