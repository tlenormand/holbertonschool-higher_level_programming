#!/usr/bin/python3
"""
class MyInt

Functions:
    add_attribute: adds a new attribute to an object if it’s possible
"""


def add_attribute(mc, attribute, value):
    """adds a new attribute to an object if it’s possible"""
    if not hasattr(mc, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(mc, attribute, value)
