#!/usr/bin/python3
"""Python class MagicClass"""


class MagicClass:
    """a magic clas"""
    def __init__(self, radius=0):
        """init the magic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """access to the area

        Return: the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """access to the circumference

        Return: the circumference"""
        return 2 * math.pi * self.__radius
