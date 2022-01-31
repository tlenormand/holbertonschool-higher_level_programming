#!/usr/bin/python3
"""
class BaseGeometry

Class:
    BaseGeometry: raise exception
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
