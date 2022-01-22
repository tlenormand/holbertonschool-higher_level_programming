#!/usr/bin/python3
"""module that prints a square with '#'"""


def print_square(size):
    """print a square with '#'

    Args:
        size: length of the square

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for y in range(size):
        for x in range(size):
            print("#", end='')
        print()
