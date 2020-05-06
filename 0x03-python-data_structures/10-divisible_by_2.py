#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    le = len(my_list)
    for item in range(le):
        if new_list[item] % 2 == 0:
            new_list[item] = True
        else:
            new_list[item] = False
    return new_list
