#!/usr/bin/python3
"""
class MyInt

Class:
    MyInt: inherits from int
"""


class MyInt(int):
    """
    class MyInt

    functions:
        __init__: init a MyInt
        __eq__: == is replaced by !=
        __ne__: != is replaced by ==
    """
    def __init__(self, value):
        """
        __init__: init a MyInt

        Args:
            value: value of MyInt
        """
        self.numbers = value

    def __eq__(self, value1):
        """== is replaced by !="""
        return self.numbers != value1

    def __ne__(self, value2):
        """!= is replaced by =="""
        return self.numbers == value2
