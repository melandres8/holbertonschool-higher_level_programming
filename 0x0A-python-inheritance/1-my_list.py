#!/usr/bin/python3
"""Mylist Class"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        print(sorted(self))
