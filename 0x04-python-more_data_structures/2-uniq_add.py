#!/usr/bin/python3
"""function that returns a set of common elements in two sets

    Return:
        the addition of all unique elemnts
"""


def uniq_add(my_list=[]):
    unique_list = []
    result = 0

    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)

    for i in unique_list:
        result += i

    return result
