#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set(set_2 & set_1)
    return new_set
