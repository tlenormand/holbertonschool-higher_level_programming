#!/usr/bin/python3
"""function that returns the weighted average of all integers tuple
(<score>, <weight>)

    Args:
        my_list: list of integer

    Return:
        average
"""


def weight_average(my_list=[]):
    coef = 0
    size = 0

    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    for i in my_list:
        coef += i[0] * i[1]
        size += i[1]

    return coef / size
