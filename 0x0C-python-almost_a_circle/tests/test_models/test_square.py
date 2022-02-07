#!/usr/bin/python3

import unittest
from models import square
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import pycodestyle
import io
from contextlib import redirect_stdout


class TestSquareClass(unittest.TestCase):

    def setUp(self):
        """reset instances"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """init the test"""
        pass

    def test_documentation(self):
        """Test the documentations of class Square"""
        len_doc = len(square.__doc__)
        self.assertGreater(len_doc, 0)

        len_doc = len(Square.__doc__)
        self.assertGreater(len_doc, 0)

        len_doc = len(Square.__init__.__doc__)
        self.assertGreater(len_doc, 0)

        len_doc = len(Square.size.__doc__)
        self.assertGreater(len_doc, 0)

        len_doc = len(Square.__str__.__doc__)
        self.assertGreater(len_doc, 0)

        len_doc = len(Square.update.__doc__)
        self.assertGreater(len_doc, 0)

        len_doc = len(Square.to_dictionary.__doc__)
        self.assertGreater(len_doc, 0)

    def test_subclass(self):
        """Test if square is a subclass of Rectangle and Base"""
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_conformance(self):
        """Test if the module Square respect PEP8"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_valid_case(self):
        """Test some valid cases with Square"""
        s1 = Square(5)
        # self.assertEqual(s1.id, 29)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

        s2 = Square(653, 54, 43, 963)
        self.assertEqual(s2.id, 963)
        self.assertEqual(s2.size, 653)
        self.assertEqual(s2.x, 54)
        self.assertEqual(s2.y, 43)
        self.assertEqual(s2.width, 653)
        self.assertEqual(s2.height, 653)

        s3 = Square(4, 3, 3, None)
        # self.assertEqual(s3.id, 30)
        self.assertEqual(s3.size, 4)
        self.assertEqual(s3.x, 3)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.width, 4)
        self.assertEqual(s3.height, 4)

    ##########################################################
    # TypeError
    ##########################################################

    def test_TypeError_no_arguments(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square()

    def test_TypeError_too_many_arguments(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(2, 2, 2, 2, 2, 2, 2, 2)

    # string

    def test_TypeError_string_size(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square("oui")

    def test_TypeError_string_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(2, "e", 2, 2)

    def test_TypeError_string_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(2, 2, "e", 2)

    # float

    def test_TypeError_float_size(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(4.5)

    def test_TypeError_float_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(2, 4.5, 2, 2)

    def test_TypeError_float_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(2, 2, 4.5, 2)

    # list
    def test_list_size(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square([1, 1])

    def test_list_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(1, [3, 3], 4)

    def test_list_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(1, 2, [4, 4])

    # tuple
    def test_tuple_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square((1, 1), 2, 3)

    def test_tuple_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(1, 2, (3, 3))

    def test_tuple_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(1, 2, (4, 4))

    # dict
    def test_dict_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square({"hello": 12}, 2, 3)

    def test_dict_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(1, {"hello": 12}, 3)

    def test_dict_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(1, 2, {"hello": 12})

    # None
    def test_None_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(None, 2, 3)

    def test_None_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(1, None, 4)

    def test_None_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Square(1, 2, None)

    ##########################################################
    # __str__
    ##########################################################

    def test___str__(self):
        """fuction that test for __str__()"""
        r1 = Square(1, 2, 0, 1212121212)
        self.assertEqual(r1.__str__(), "[Square] (1212121212) 2/0 - 1")

    ##########################################################
    # area
    ##########################################################

    def test_area(self):
        """fuction that test for area()"""
        r1 = Square(12)
        self.assertEqual(r1.area(), 144)

    ##########################################################
    # display
    ##########################################################

    def test_diplay(self):
        """Check display func"""
        r1 = Square(8)
        r2 = Square(8, 7, 3)
        with io.StringIO() as buf, redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 8 + "\n") * 8)
        with io.StringIO() as buf, redirect_stdout(buf):
            r2.display()
            output = buf.getvalue()
            self.assertEqual(output, (3 * "\n" + (" " * 7 + "#" * 8 + "\n") * 8))

    ##########################################################
    # update
    ##########################################################

    def test_update(self):
        """fuction that test for update()"""
        r1 = Square(7, 3, 2, 4)
        r1.update(1234567890, 1, 2, 3)

        self.assertEqual(r1.id, 1234567890)
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)

        r1.update(size=131)
        self.assertEqual(r1.size, 131)
        self.assertEqual(r1.width, 131)
        self.assertEqual(r1.height, 131)

        r1.update(size=454, y=1)
        self.assertEqual(r1.size, 454)
        self.assertEqual(r1.width, 454)
        self.assertEqual(r1.height, 454)
        self.assertEqual(r1.y, 1)

        r1.update()
        self.assertEqual(r1.height, 454)

    def test_update_error(self):
        """Function to test different error case of uptdate"""
        r1 = Square(7, 3, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(1, "str")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(1, [1, 2])
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(1, -1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(1, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 1, "str")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 1, [1, 2])
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(1, 1, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 1, 1, "str")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 1, 1, [1, 2])
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(1, 1, 1, -1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size="str")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size=[1, 2, 3])
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(size=-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(size=0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x="str")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=[1, 2, 3])
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(x=-1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y="str")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=[1, 2, 3])
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(y=-1)

    def test_updateTooMuchArg(self):
        """Test update with to much arg"""
        r1 = Square(8, 7, 3, 4)
        self.assertEqual(str(r1), "[Square] (4) 7/3 - 8")
        # r1.update(4, 3, 2, 1, 0, 2)
        # self.assertEqual(str(r1), "[Square] (4) 2/1 - 3")

    def test_updateWithoutArg(self):
        """Test update with no arg"""
        r1 = Square(8, 7, 3, 2)
        r1.update()
        self.assertEqual(str(r1), "[Square] (2) 7/3 - 8")

    def test_updateRandomKwarg(self):
        """Test update with random Kwarg"""
        r1 = Square(8, 7, 3, 2)
        r1.update(ThomasLeBoss="Non")
        self.assertEqual(str(r1), "[Square] (2) 7/3 - 8")

    ##########################################################
    # to_dictionary
    ##########################################################

    def test_to_dictionary(self):
        """fuction that test for to_dictionary()"""
        r1 = Square(1, 2, 3, 1234567890)
        r2 = Square(1, 3, 4, None)
        r3 = Square(1)
        self.assertEqual(
            r1.to_dictionary(),
            {"id": 1234567890, "x": 2, "size": 1, "y": 3},
        )
        self.assertEqual(
            r2.to_dictionary(),
            {"id": 1, "x": 3, "size": 1, "y": 4},
        )
        self.assertEqual(
            r3.to_dictionary(),
            {"id": 2, "x": 0, "size": 1, "y": 0},
        )

    ##########################################################
    # create
    ##########################################################

    def test_create(self):
        """Test create a rectangle"""
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertNotEqual(r1, r2)
        self.assertIsNot(r1, r2)

    ##########################################################
    # save_to_file | load_from_file || save_to_file_csv | load_form_file_csv
    ##########################################################

    def test_saveToFile_loadFromFile(self):
        """Check the both saveto, and loadfrom function to a json file"""
        r1 = Square(1, 2, 3, 4)
        r2 = Square(1, 2, 3, 4)
        listOfRectsInput = [r1, r2]
        Square.save_to_file(listOfRectsInput)
        listOfRectsOutput = Square.load_from_file()
        self.assertEqual(
            listOfRectsInput[0].to_dictionary(), listOfRectsOutput[0].to_dictionary()
        )
        self.assertEqual(
            listOfRectsInput[1].to_dictionary(), listOfRectsOutput[1].to_dictionary()
        )

    def test_saveToFile_loadFromFile_empty(self):
        """Check the both saveto, and loadfrom function to a json file"""
        listOfRectsInput = []
        Square.save_to_file(listOfRectsInput)
        listOfRectsOutput = Square.load_from_file()
        self.assertEqual(
            listOfRectsInput, listOfRectsOutput
        )

    def test_saveToCSV_loadFromCSV(self):
        """Check the both saveto, and loadfrom function to a csv file"""
        r1 = Square(1, 2, 3, 4)
        r2 = Square(1, 2, 3, 4)
        listOfRectsInput = [r1, r2]
        Square.save_to_file_csv(listOfRectsInput)
        listOfRectsOutput = Square.load_from_file_csv()
        self.assertEqual(
            listOfRectsInput[0].to_dictionary(), listOfRectsOutput[0].to_dictionary()
        )
        self.assertEqual(
            listOfRectsInput[1].to_dictionary(), listOfRectsOutput[1].to_dictionary()
        )

    def test_saveToCSV_loadFromCSV_empty(self):
        """Check the both saveto, and loadfrom function to a csv file"""
        listOfRectsInput = []
        Square.save_to_file_csv(listOfRectsInput)
        listOfRectsOutput = Square.load_from_file_csv()
        self.assertEqual(
            listOfRectsInput, listOfRectsOutput
        )

if __name__ == "__main__":
    unittest.main()
