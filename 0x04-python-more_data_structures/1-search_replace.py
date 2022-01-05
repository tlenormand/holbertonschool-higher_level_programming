#!/usr/bin/python3
"""function that replaces all occurrences of an element
by another in a new list

    Args:
        my_list: the initial list
        search: the element to replace in the list
        replace: the new element

    Return:
        new list with all occurences replaced
"""


def search_replace(my_list, search, replace):
    new_list = my_list.copy()

    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list[i] = replace

    return new_list
