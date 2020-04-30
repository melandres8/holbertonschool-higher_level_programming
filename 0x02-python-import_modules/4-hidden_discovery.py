#!/usr/bin/python3
import hidden_4
import re

if __name__ == '__main__':
    patron = re.compile('__')
    lista = dir(hidden_4)

    for item in lista:
        m = patron.search(item)
        if m:
            lista.remove(item)
        else:
            print(item)
