#!/usr/bin/python3
""" writing an object to a text file
    using JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """Function
    """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
