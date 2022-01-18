#!/usr/bin/python3
"""Square class file"""


class Square:
    """
    class Square that defines a square

    Attributes:
        __size: size of a side of the square
    """
    # initialisation of an object size
    def __init__(self, size):
        """
        Init a square

        Args:
            size (int): size of the square

        Returns: None
        """
        self.__size = size
