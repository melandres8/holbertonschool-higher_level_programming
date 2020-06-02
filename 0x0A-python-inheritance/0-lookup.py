#!/usr/bin/python3
"""Funtion that returns a list of attr and methods"""


def lookup(obj):
    """returns the list of available
    attributes and methods of an object"""

    return dir(obj)
