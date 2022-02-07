#!/usr/bin/python3
"""
module that contain the base Square

Class:
    Square: this is the Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    this is the Square class

    Functions:
        __init__: init a Square
        __str__: print the Square as:
            [Square] (<id>) <x>/<y> - <size>
        update: assigns an argument to each attribute

    Getter:
        size: access to size

    Setter:
        size: change the size
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        init a Square

        Arguments:
            size: size of the Square
            x: x of the Square
            y: y of the Square

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        print the Square as: [Square] (<id>) <x>/<y> - <size>

        Returns:
            [Square] (<id>) <x>/<y> - <size>
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            __class__.__name__,
            self.id,
            self.x,
            self.y,
            self.size,
            )

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        if args is not None:
            - 1st argument should be the id attribute
            - 2nd argument should be the size attribute
            - 3rd argument should be the x attribute
            - 4th argument should be the y attribute
        else:
            use kwargs

        Arguments:
            args: list of args to update
            kwargs: dict of attribute to update

        Returns:
            None
        """
        arg_list = ["id", "size", "x", "y", "\0"]

        if (len(args)):
            for i in range(len(args)):
                if args[1]:
                    self.width = args[1]
                    self.height = args[1]
                setattr(self, arg_list[i], args[i])

        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """
        function that returns the dictionary representation of a Square

        Returns:
            dictionary representation of a Square
        """
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.size}

    @property
    def size(self):
        """
        access to size

        Returns:
            the size of the Rectangle
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        change the size

        Arguments:
            value: value of the new size

        Returns:
            None
        """
        self.check_value("width", value)
        self.width = value
        self.height = value
