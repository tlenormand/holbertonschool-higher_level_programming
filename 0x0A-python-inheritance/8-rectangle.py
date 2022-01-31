#!/usr/bin/python3
"""
class BaseGeometry

Class:
    BaseGeometry: raise exception
    Rectangle: class Rectangle that inherits from BaseGeometry
"""


class BaseGeometry:
    """
    raise exception

    Functions:
        area: raise exception
        integer_validator: function that validates value
    """
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


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
