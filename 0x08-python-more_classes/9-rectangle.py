#!/usr/bin/python3
"""Rectangle class file"""


class Rectangle:
    """
    class Rectangle that defines a Rectangle

    Atributes:
        __width: the width of the Rectangle
        __height: the height of the Rectangle
        number_of_instances: the number of instances
        print_symbol: symbole using to print the Rectangle

    Functions:
        __init__: initialise a Rectangle
        __del__: delete the instance of Rectangle
        __str__: print the Rectangle with the character #
        __repr__: returns a string representation of the rectangle
        area: returns the Rectangle area
        perimeter: returns the Rectangle perimeter

    @property
        width: access to width
        height: access to height

    @atribute.setter
        width: change the width
        height: change the height

    @staticmethod:
        bigger_or_equal: returns the biggest rectangle based on the area

    @classmethod:
        square: returns a new Rectangle instance with width == height == size
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Init a Rectangle

        Args:
            width (int): width of the Rectangle
            height (tuple): height of the Rectangle

        Returns: None
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        delete the instance of Rectangle

        Returns: None
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """
        print the Rectangle with the character #

        Returns: a string containing the Rectangle with the character #
        """
        str_rectangle = ""

        if not self.__height or not self.__width:
            return ""

        for y in range(self.__height):
            for x in range(self.__width):
                str_rectangle += str(self.print_symbol)
            if y < self.__height - 1:
                str_rectangle += '\n'

        return str_rectangle

    def __repr__(self):
        """
        returns a string representation of the rectangle

        Returns: string representation of the rectangle
        """
        repr_rectangle = "Rectangle({:d}, {:d})".format(self.__width,
                                                        self.__height)

        return repr_rectangle

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area

        Returns: the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def area(self):
        """
        returns the Rectangle area

        Returns: the Rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        returns the Rectangle perimeter

        Returns: the Rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__height + self.__width)

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance with width == height == size

        Returns: new Rectangle instance with width == height == size
        """
        return Rectangle(size, size)
