#!/usr/bin/python3
"""Square class"""


class Square():
    """Validating if size is an instance
    and if is greater and equal to 0
    Attributes:
        attr1 (int): size is a main attr of a square
    """
    def __init__(self, size=0):
        """isinstance function checks if
        the object is an instance or subclass
        of the second argument

        Args:
            size (int): size of my square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """Returning the Area of a square"""
    def area(self):
        return int(self.__size) * int(self.__size)
