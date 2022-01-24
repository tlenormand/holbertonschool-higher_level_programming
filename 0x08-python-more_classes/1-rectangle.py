#!/usr/bin/python3
"""Rectangle class file"""


class Rectangle:
    """
    class Rectangle that defines a Rectangle

    Atributes:
        __width: the width of the Rectangle
        __height: the height of the Rectangle

    Functions:
        __init__: initialise a Rectangle

    @property
        width: access to width
        height: access to height

    @atribute.setter
        width: change the width
        height: change the height

    """
    def __init__(self, width=0, height=0):
        """
        Init a Rectangle

        Args:
            width (int): width of the Rectangle
            height (tuple): height of the Rectangle

        Returns: None
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        access to width

        Returns: the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        change the width

        args:
            value: value of the new width

        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        access to height

        Returns: the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        change the height

        args:
            value: value of the new height

        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
