#!/usr/bin/python3
""" Adds all arguments to a
    python list
"""
from sys import argv


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

arguments = argv[1:]
try:
    load = load_from_json_file('add_item.json')
except:
    load = []
save_to_json_file(load + arguments, 'add_item.json')
