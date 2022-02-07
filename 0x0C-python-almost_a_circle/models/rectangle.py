#!/usr/bin/python3
"""
module that contain the base Rectangle

Class:
    Rectangle: this is the Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """
    this is the Rectangle class

    Functions:
        __init__: init a rectangle
        __str__: print the Rectangle as:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        check_value: function that check if value has good parameters
        area: function that returns the Rectangle area
        display: function that print the Rectangle with the character #
            by taking care of x and y
        update: assigns an argument to each attribute
        to_dictionary: function that returns the dictionary representation
            of a Rectangle

    Getter:
        width: access to width
        height: access to height
        x: access to x
        y: access to y

    Setter:
        width: change the width
        height: change the height
        x: change the x
        y: change the y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init a rectangle

        Arguments:
            width: width of the Rectangle
            height: height of the Rectangle
            x: x of the Rectangle
            y: y of the Rectangle

        Returns:
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        print the Rectangle as: [Rectangle] (<id>) <x>/<y> - <width>/<height>

        Returns:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            __class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
            )

    def check_value(self, name, value):
        """
        function that check if value has good parameters

        Arguments:
            name: name of the value to check
            value: value to check

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if (name == "x" or name == "y") and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """
        function that returns the Rectangle area

        Returns:
            the Rectangle area
        """
        return self.height * self.width

    def display(self):
        """
        function that print the Rectangle with the character #
        by taking care of x and y

        Returns:
            None
        """
        for y in range(self.y):
            print()

        for j in range(self.height):
            for x in range(self.x):
                print(" ", end='')
            for i in range(self.width):
                print("#", end='')
            if j < self.height - 1:
                print()
        print()

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        if args is not None:
            - 1st argument should be the id attribute
            - 2nd argument should be the width attribute
            - 3rd argument should be the height attribute
            - 4th argument should be the x attribute
            - 5th argument should be the y attribute
        else:
            use kwargs

        Arguments:
            args: list of args to update
            kwargs: dict of attribute to update

        Returns:
            None
        """
        rectangle_list = ["id", "width", "height", "x", "y", "\0"]

        for i in range(len(args)):
            setattr(self, rectangle_list[i], args[i])

        if not args:
            for i, Value in kwargs.items():
                if i in rectangle_list:
                    setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """
        function that returns the dictionary representation of a Rectangle

        Returns:
            dictionary representation of a Rectangle
        """
        return {'id': self.id, "width": self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    @property
    def width(self):
        """
        access to width

        Returns:
            the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        change the width

        Arguments:
            value: value of the new width

        Returns:
            None
        """
        self.check_value("width", value)
        self.__width = value

    @property
    def height(self):
        """
        access to height

        Returns:
            the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        change the height

        Arguments:
            value: value of the new height

        Returns:
            None
        """
        self.check_value("height", value)
        self.__height = value

    @property
    def x(self):
        """
        access to x

        Returns:
            the x of the Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        change the x

        Arguments:
            value: value of the new x

        Returns:
            None
        """
        self.check_value("x", value)
        self.__x = value

    @property
    def y(self):
        """
        access to y

        Returns:
            the y of the Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        change the y

        Arguments:
            value: value of the new y

        Returns:
            None
        """
        self.check_value("y", value)
        self.__y = value
