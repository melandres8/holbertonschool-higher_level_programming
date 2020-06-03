#!/usr/bin/python3
""" Reading n lines of a text file UTF-8
"""


def read_lines(filename="", nb_lines=0):
    """ Printing n lines of a text file
    """
    with open(filename, 'r') as file:
        if 0 > nb_lines < len(open(filename).readlines()):
            while nb_lines:
                print(file.readline(), end='')
                nb_lines -= 1
        else:
            print(file.read(), end='')
            print()
