#!/usr/bin/python3
"""
module add two integers

functions:
    add_integer: add two integers
"""


def add_integer(a, b=98):
    """add two integers

    Args:
        a: first integer
        b: second integer

    Returns:
        the return value. a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)
