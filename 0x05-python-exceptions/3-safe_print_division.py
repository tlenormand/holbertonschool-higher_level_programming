#!/usr/bin/python3
"""function that divides 2 integers and prints the result

    Args:
        a: first integer
        b: second integer

    Return:
        value of the division, otherwise: None
"""


def safe_print_division(a, b):

    try:
        result = a / b
    except ZeroDivisionError:
        result = "None"
    finally:
        print("Inside result: {}".format(result))

    return result
