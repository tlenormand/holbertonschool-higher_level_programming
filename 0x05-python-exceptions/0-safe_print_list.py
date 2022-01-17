#!/usr/bin/python3
"""function that prints x elements of a list

    Args:
        my_list: list to print
        x: number of elements to print

    Return:
        number of elements printed
"""


def safe_print_list(my_list=[], x=0):

    idx = 0

    while x > 0:

        try:
            print("{:d}".format(my_list[idx]), end='')
            x -= 1
            idx += 1
        except Exception:
            print()
            return idx

    print()

    return idx
