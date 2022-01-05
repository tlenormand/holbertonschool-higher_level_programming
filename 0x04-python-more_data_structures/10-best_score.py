#!/usr/bin/python3
"""function that returns a key with the biggest integer value

    Args:
        a_dictionary: dictionnary

    Return:
        key with the biggest integer value
"""


def best_score(a_dictionary):
    biggest = 0

    if not a_dictionary:
        return "None"

    for idx in a_dictionary:
        if a_dictionary[idx] > biggest:
            biggest = a_dictionary[idx]
            name = idx

    return name
