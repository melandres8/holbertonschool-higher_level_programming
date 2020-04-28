#!/usr/bin/python3
for item in range(0, 100):
    if item == 99:
        print("{}".format(item), end="\n")
    else:
        print("{:02d}".format(item), end=", ")
