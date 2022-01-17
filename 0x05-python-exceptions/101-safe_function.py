#!/usr/bin/python3
import sys

"""function that executes a function safely

    Args:
        a: first integer
        b: second integer

    Return:
        value of the division, otherwise: None
"""


def safe_function(fct, *args):

    try:
        result = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        result = None

    return (result)
