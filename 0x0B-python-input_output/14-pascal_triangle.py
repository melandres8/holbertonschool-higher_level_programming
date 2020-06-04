#!/usr/bin/python3
""" Pascal module
"""


def pascal_triangle(n):
    """ Returning a list of lists
        of integer representing
        the pascal's triangle of n
    """
    my_list = []
    if n <= 0:
        return my_list
    for item1 in range(1, n + 1):
        number = 1
        row = []
        for item2 in range(1, item1 + 1):
            row += [number]
            number = number * (item1 - item2) // item2
        my_list += [row]
    return my_list
