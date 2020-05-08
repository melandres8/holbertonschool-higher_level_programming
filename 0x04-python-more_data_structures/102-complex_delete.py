#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k = [key for key, v in a_dictionary.items() if v is value]
    if k:
        for item in k:
            a_dictionary.pop(item)
    return a_dictionary
