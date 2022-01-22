#!/usr/bin/python3
"""
Unittest for "max_integer(list=[])"

Execute: python3 -m unittest tests.6-max_integer_test
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class that test the max integer function

    functions:
        test_integers: fuction that test for integers
        test_floats: function that test for floats
        test_None: function that test for empty list
        test_string: function that test for a string
        test_TypeError: function that test for a TypeError
    """
    def test_integers(self):
        """
        fuction that test for integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 1]), 5)
        self.assertEqual(max_integer([12, 23, 23, 54, 53, 11, 123, 5467, 45,
                                      3, 0, -2]), 5467)
        self.assertEqual(max_integer([-3, -7, -1, -98, -7878, -76]), -1)
        self.assertEqual(max_integer([-3, -3, -3]), -3)
        self.assertEqual(max_integer([-4, -3, -3, -3, -4]), -3)

    def test_floats(self):
        """
        function that test for floats
        """
        self.assertEqual(max_integer([1.1, 3.3, 6.4, 4.2]), 6.4)
        self.assertEqual(max_integer([-12.4, -75.3, -2.564]), -2.564)
        self.assertEqual(max_integer((1, 2, 3)), 3)

    def test_None(self):
        """
        function that test for empty list
        """
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)

    def test_string(self):
        """
        function that test for a string
        """
        self.assertEqual(max_integer("hello"), "o")
        self.assertEqual(max_integer(["a", "String", "Hello!", "123"]), "a")

    def test_TypeError(self):
        """
        function that test for a TypeError
        """
        with self.assertRaises(TypeError):
            max_integer(1)
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([1, 2, None])
        with self.assertRaises(TypeError):
            max_integer([1, 2, "hello"])


if __name__ == '__main__':
    unittest.main()
