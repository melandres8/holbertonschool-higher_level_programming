#!/usr/bin/python3
"""
    Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
        Return a division of all elements in a list

        Args:
            matrix: (list) list of lists of numbers
            div: (int) divider
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for row in matrix:
        for number in row:
            if type(number) != int and type(number) != float:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [list(map(lambda n: round(n / div, 2), row)) for row in matrix]
