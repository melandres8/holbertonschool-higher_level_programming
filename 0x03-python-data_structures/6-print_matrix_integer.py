#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
            print(' '.join("{:d}".format(i) for i in item))
