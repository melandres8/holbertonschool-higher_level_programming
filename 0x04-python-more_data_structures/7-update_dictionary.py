#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key:
        a_dictionary[key] = value
    if not key:
        a_dictionary[key] = value
    return a_dictionary
