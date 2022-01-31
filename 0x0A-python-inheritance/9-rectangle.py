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
        __str__: return the following rectangle description:
            [Rectangle] <width>/<height>
        area: calculate the area
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

    def __str__(self):
        """
        return the following rectangle description:
            [Rectangle] <width>/<height>

        Returns: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """
        calculate the area

        Returns:
            area of the Rectangle
        """
        return self.__width * self.__height
