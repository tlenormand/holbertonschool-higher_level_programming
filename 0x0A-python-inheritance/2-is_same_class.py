#!/usr/bin/python3
"""
file check if object is instance of a class

Functions:
    is_same_class: function that check if an obect is an instance of my class
"""


def is_same_class(obj, a_class):
    """
    function that check if an obect is an instance of my class

    Args:
        obj: the object to check
        a_class: class to check

    Returns:
        True: if the object is exactly an instance of the specified class
        False: otherwise
    """
    return type(obj) is a_class
