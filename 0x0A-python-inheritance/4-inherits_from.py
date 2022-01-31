#!/usr/bin/python3
"""
file that check if an obect is an instance of a class that
inherited (directly or indirectly) from the specified class

Functions:
    inherits_from: function that check if an obect is an instance of a
    class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    function that check if an obect is an instance of a class that
    inherited (directly or indirectly) from the specified class

    Args:
        obj: the object to check
        a_class: class to check

    Returns:
        True: if the object is an instance
        False: otherwise
    """
    return type(obj) is not a_class
