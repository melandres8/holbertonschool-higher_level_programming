#!/usr/bin/python3
"""
    printing my first and last name function.
"""


def say_my_name(first_name, last_name=""):
    """
        This function print last and first name.

        Args:
            first_name: (string) get the first name
            last_name: (string) get the last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name != "" or last_name != "":
        pass
    print("My name is {:s} {:s}".format(first_name, last_name))
