#!/usr/bin/python3
"""Square class"""


class Square():
    def __init__(self, size=0):

        """isinstance function checks if
        the object is an instance or subclass
        of the second argument
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
