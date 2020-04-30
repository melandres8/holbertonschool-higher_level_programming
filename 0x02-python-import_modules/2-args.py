#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    argv.remove(argv[0])
    if len(argv) is 0:
        print("{:d} arguments.".format(len(argv)))
    elif len(argv) is 1:
        print("{:d} argument:".format(len(argv)))
    else:
        print("{:d} arguments:".format(len(argv)))

    for index, item in enumerate(argv):
        print("{:d}: {}".format(index + 1, item))
