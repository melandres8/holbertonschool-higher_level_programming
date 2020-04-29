#!/usr/bin/python3
def listToString(lista):
    str1 = ""
    for item in lista:
        str1 += item
    return str1


def remove_char_at(str, n):
    lista1 = []
    for index, char in enumerate(str):
        if index != n:
            lista1.append(char)
    return listToString(lista1)
