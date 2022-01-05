#!/usr/bin/python3
"""function that returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: dictionnary

    Return:
        the dictionnary with all values multiplied by 2
"""


def multiply_by_2(a_dictionary):
    new_dictionnary = a_dictionary.copy()

    new_dictionnary.update((x, y*2) for x, y in new_dictionnary.items())

    return new_dictionnary
