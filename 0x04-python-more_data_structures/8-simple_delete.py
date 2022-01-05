#!/usr/bin/python3
"""function that deletes a key in a dictionary

    Args:
        a_dictionary: dictionnary
        key: key of the dictionnary to deleted

    Return:
        the dictionnary updated
"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
