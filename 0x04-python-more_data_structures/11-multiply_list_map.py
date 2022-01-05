#!/usr/bin/python3
"""function that returns a list with all values multiplied by a number
without using any loops

    Args:
        my_list: first list
        number: multiplier

    Return:
        new list multiplied by "number"
"""


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
