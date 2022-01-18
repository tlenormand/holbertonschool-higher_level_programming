#!/usr/bin/python3
"""class Square that defines a square

Attributes:
    __size: size of a side of the square
"""


class Square:
    # initialisation of an object size
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    # calculation of the area
    def area(self):
        return self.__size * self.__size

    # prints in stdout the square with the character '#'
    def my_print(self):
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()

    @property
    # return his private attribute size
    def size(self):
        return self.__size

    @size.setter
    # change the value of his private attribute size
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
