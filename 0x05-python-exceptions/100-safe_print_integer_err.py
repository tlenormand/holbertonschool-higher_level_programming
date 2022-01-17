#!/usr/bin/python3
import sys

"""function that prints an integer

    Args:
        value: value to print

    Return:
        true if value has been correctly printed, false otherwise
"""


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False

    return True
