#!/usr/bin/python3
def uppercase(str):
    for item in str:
        uniCode = ord(item)
        if uniCode >= 97 and uniCode <= 122:
            item = chr(uniCode - 32)
        print("{}".format(item), end="")
    print("")
