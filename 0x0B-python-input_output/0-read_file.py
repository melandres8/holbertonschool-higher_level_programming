#!/usr/bin/python3
""" Function that reading a file
"""


def read_file(filename=""):
    with open(filename, 'r') as file:
        print(file.read())
