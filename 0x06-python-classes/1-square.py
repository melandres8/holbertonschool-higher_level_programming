#!/usr/bin/python3
class Square:
    """__init__ always runs when we create
    a new object of a class"""
    def __init__(self, size=0):
        """Creating a private instance"""
        self.__size = size
