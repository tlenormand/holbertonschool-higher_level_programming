#!/usr/bin/python3
"""function that finds all multiples of 2 in a list"""


def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2:
            new_list[i] = False
        else:
            new_list[i] = True
    return new_list
