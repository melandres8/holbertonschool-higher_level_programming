#!/usr/bin/python3
"""Operators"""


class MyInt(int):
    """ MyInt class
    """
    def __eq__(self, number):
        """Using 'real' attribute from int"""
        return self.real != number

    def __ne__(self, number):
        return self.real == number
