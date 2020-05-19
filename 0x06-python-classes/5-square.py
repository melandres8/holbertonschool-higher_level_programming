#!/usr/bin/python3
class Square:

    """__init__ constructor: Runs always when we
    create a new instance of a class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return int(self.__size) * int(self.__size)

    """Printing a Square and validating
    if the size is 0 or not"""
    def my_print(self):
        for row in range(self.__size):
            print('#' * self.__size)
        if self.__size == 0:
            print()
