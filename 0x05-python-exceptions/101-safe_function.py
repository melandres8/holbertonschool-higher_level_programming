#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    div = None
    try:
        div = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
    return div
