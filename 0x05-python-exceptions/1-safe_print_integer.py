#!/usr/bin/python3
"""function that prints an integer with "{:d}".format()

    Args:
        value: integer to print

    Return:
        true if value has been correctly printed, false otherwise
"""


def safe_print_integer(value):

    try:
        print("{:d}".format(value))
    except Exception:
        return False

    return True
