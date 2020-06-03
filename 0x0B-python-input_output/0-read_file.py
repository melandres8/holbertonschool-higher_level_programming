#!/usr/bin/python3
""" Function that reading a file
"""


def read_file(filename=""):
    """Print an entire file text
    """
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')
        print()
