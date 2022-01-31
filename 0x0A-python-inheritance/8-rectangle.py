#!/usr/bin/python3
"""
class BaseGeometry

Class:
    BaseGeometry: raise exception
    Rectangle: class Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry

    Functions:
        __init__: init a Rectangle
    """
    def __init__(self, width, height):
        """
        init a Rectangle

        Args:
            width: width of the Rectangle
            height: height of the rectangle

        Returns: None
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
