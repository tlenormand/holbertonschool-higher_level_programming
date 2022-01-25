#!/usr/bin/python3
"""
LockedClass class file
prevents the user from dynamically creating new instance attributes
"""


class LockedClass:
    """
    class LockedClass that prevents the user from dynamically
    creating new instance attributes

    Atributes:
        first_name: first name

    Functions:
        __init__: initialise a LockedClass
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=0):
        """
        Init a LockedClass

        Args:
            first_name: first name of LockedClass

        Returns: None
        """
        self.first_name = first_name
