#!/usr/bin/python3
"""
class BaseGeometry

Class:
    BaseGeometry: raise exception
    Rectangle: class Rectangle that inherits from BaseGeometry
        Square: inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle

    Functions:
        __init__: init a Square
        area: calculate the area of the square
    """
    def __init__(self, size):
        """
        init a Square

        args:
            Size: size of the Square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        calculate the area

        Returns:
            area of the Square
        """
        return self.__size ** 2
