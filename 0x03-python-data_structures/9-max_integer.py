#!/usr/bin/python3
"""function that finds the biggest integer of a list"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    return (sorted(my_list)[-1])
