#!/usr/bin/python3
""" JSON module
"""
import json


def from_json_string(my_str):
    """ Object represented by a JSON
    string
    """
    return json.loads(my_str)
