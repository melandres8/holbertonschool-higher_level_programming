#!/usr/bin/python3
"""Append module"""


def append_write(filename="", text=""):
    """ Appending a string into a file
    """
    with open(filename, 'a') as file:
        return file.write(text)
