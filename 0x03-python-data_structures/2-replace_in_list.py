#!/usr/bin/python3
"""function that replaces an element of a list at a specific position"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list
    new_list[idx] = element
    return new_list
