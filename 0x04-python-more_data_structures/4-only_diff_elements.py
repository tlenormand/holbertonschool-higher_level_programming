#!/usr/bin/python3
"""function that returns a set of all elements present in only one set

    Args:
        set_1: first set
        set_2: second set

    Return:
        set of all elements present in only one set
"""


def only_diff_elements(set_1, set_2):
    set_3 = []

    for element in set_1:
        if element not in set_2:
            set_3.append(element)

    for element in set_2:
        if element not in set_1:
            set_3.append(element)

    return set_3
