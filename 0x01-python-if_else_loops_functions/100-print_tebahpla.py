#!/usr/bin/python3
for item in range(122, 96, -1):
    uniCode = ord(chr(item))
    if uniCode % 2 == 0:
        alph = chr(uniCode)
        print(alph, end="")
    elif uniCode % 2 == 1:
        alph = chr(uniCode - 32)
        print(alph, end="")
