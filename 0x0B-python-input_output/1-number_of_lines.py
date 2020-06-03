#!/usr/bin/python3
""" Function that return the number of lines
in a given file
"""


def number_of_lines(filename=""):
    """ Returning the number of line
        in a text file
    """
    with open(filename, 'r') as file:
        n_lines = 0
        for line in file:
            n_lines += 1
    return n_lines
