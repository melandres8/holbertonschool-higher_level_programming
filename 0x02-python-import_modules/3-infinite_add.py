#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    ind = 0
    argv.remove(argv[0])
    if len(argv) is 0:
        print("{:d}".format(len(argv)))
    else:
        for index in argv:
            ind += int(index)
        print("{}".format(ind))
