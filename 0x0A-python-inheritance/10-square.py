#!/usr/bin/python3
"""
class BaseGeometry

Class:
    BaseGeometry: raise exception
    Rectangle: class Rectangle that inherits from BaseGeometry
        Square: inherits from Rectangle
"""


class BaseGeometry:
    """
    raise exception

    Functions:
        area: raise exception
        integer_validator: function that validates value
    """
    def area(self):
        """
        calculate the area

        Returns:
            area of the Rectangle
        """
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """function that validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry

    Class:
        Square: inherits from Rectangle

    Functions:
        __init__: init a Rectangle
        __str__: return the following rectangle description: [Rectangle] <widt\
h>/<height>
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
        return the following rectangle description: [Rectangle] <width>/<heigh\
t>

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
