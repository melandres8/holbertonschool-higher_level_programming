#!/usr/bin/python3
"""Square class"""


class Square():
    """__init__ constructor: Runs always when we
    create a new instance of a class
    Attributes:
    attr1 (int): is the size of a square
    attr2 (tuple): position
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Inicializing my class with

        Args:
            size (int): size of a square
            position (tuple): position
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter, retrieve the size of a square
        this methods is useful to handle with
        privacity of our instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Handle the value of a size if
        is an integer or not

        Args:
            position (tuple): position of a square
        """
        if (value[1] < 0 or value[0] < 0 or not isinstance(value, tuple)
                or len(value) != 2 or not isinstance(value[0], int) or
                not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculating the area of a square"""
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """Printing a Square and validating
        if the size is 0 or not"""
        pos = self.__position
        for item in range(pos[1]):
            print()
        for row in range(self.__size):
            print("{}{}".format(' ' * pos[0], '#' * self.__size))
        if self.__size == 0:
            print()
