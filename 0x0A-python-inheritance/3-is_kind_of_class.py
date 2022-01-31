#!/usr/bin/python3
"""
file check if object is instance of a class or
if the object is an instance of a class that inherited from

Functions:
    is_kind_of_class: function that check if an obect is an instance of
    my class or if the object is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    function that check if an obect is an instance of my class or
    if the object is an instance of a class that inherited from

    Args:
        obj: the object to check
        a_class: class to check

    Returns:
        True: if the object is an instance
        False: otherwise
    """
    return isinstance(obj, a_class)
