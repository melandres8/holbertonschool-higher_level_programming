#!/usr/bin/python3
def no_c(my_string):
    trans = {ord('c'): '', ord('C'): ''}
    return my_string.translate(trans)
