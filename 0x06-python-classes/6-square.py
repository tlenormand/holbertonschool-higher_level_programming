#!/usr/bin/python3
"""Square class file"""


class Square:
    """
    class Square that defines a square

    Attributes:
        __size: size of a side of the square
    """
    # initialisation of the Square class
    def __init__(self, size=0, position=(0, 0)):
        """
        Init a square

        Args:
            size (int): size of the square
            position (tuple): start position of the Square

        Returns: None
        """
        # initialisation of an object size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        # initialisation of an object position
        tuple_check = True
        if not isinstance(position, tuple):
            tuple_check = False
        else:
            for i in range(0, len(position)):
                if not isinstance(position[i], int) or position[i] < 0:
                    tuple_check = False

        if tuple_check and i == 1:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    # calculation of the area
    def area(self):
        """
        square area

        Returns: the current square area
        """
        return self.__size * self.__size

    # prints in stdout the square with the character '#'
    def my_print(self):
        """
        print the Square in '#' on stdout

        Returns: the size of the Square
        """
        if not self.__size:
            print()
        else:
            for y in range(self.__position[1]):
                print(' ')

            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()

    @property
    # return his private attribute size
    def size(self):
        """
        access to size

        Returns: the size of the Square
        """
        return self.__size

    @property
    # return his private attribute position
    def position(self):
        """
        access to position

        Returns: the position of the Square
        """
        return self.position

    @size.setter
    # change the value of his private attribute size
    def size(self, value):
        """
        change the size

        args:
            value: value of the new size

        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    # change the value of his private attribute position
    def position(self, value):
        """
        change the position

        args:
            value: value of the new position

        Returns: None
        """
        tuple_check = True
        if not isinstance(value, tuple):
            tuple_check = False
        else:
            for i in range(0, len(value)):
                if not isinstance(value[i], int) or value[i] < 0:
                    tuple_check = False

        if tuple_check and i == 1:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
