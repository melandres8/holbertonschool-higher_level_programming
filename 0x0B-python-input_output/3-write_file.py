#!/usr/bin/python3
""" write_file module
"""


def write_file(filename="", text=""):
    """ Writing text into a text file
    """
    with open(filename, 'w') as file:
        file.write(text)
        return text
