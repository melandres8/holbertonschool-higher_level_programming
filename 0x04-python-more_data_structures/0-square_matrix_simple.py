#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for item in matrix:
        power = lambda x: x ** 2
        new_matrix += [[power(x) for x in item]]
    return new_matrix
