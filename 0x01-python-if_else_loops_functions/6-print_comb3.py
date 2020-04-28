#!/usr/bin/python3
for item in range(10):
    for item2 in range(item + 1, 10):
        if item != item2:
            print("{}".format(item), end="")
            if item == 8 and item2 == 9:
                print("{}".format(item2))
            else:
                print("{}".format(item2), end=", ")
