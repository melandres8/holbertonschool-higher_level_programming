#!/usr/bin/python3
def power(b, x):
    return b ** x


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for item in matrix:
        new_matrix += [[power(n, 2) for n in item]]
    return new_matrix
