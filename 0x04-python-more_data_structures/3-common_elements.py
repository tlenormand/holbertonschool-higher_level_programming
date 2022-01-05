#!/usr/bin/python3
"""function that returns a set of common elements in two sets

    Args:
        set_1: first set
        set_2: second set

    Return:
        the common element
"""


def common_elements(set_1, set_2):
    for element in set_1:
        if element in set_2:
            return list(element)
