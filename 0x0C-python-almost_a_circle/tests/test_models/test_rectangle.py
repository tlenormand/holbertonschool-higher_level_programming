#!/usr/bin/python3
"""
Unittest for "rectangle.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_rectangle.py
"""

import unittest
import pycodestyle
from models.base import Base
from models import rectangle
from os.path import exists
import io
from contextlib import redirect_stdout
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):

    """
    class that test the max integer function
    ValueError:
        negative width
        negative height
        negative x
        negative y
        zero width
        zero height
    TypeError:
        too many arguments
        too few arguments
        string width
        string height
        string x
        string y
        float width
        float height
        float x
        float y
        list width
        list height
        list x
        list y
        tuple width
        tuple height
        tuple x
        tuple y
        dict width
        dict height
        dict x
        dict y
        None width
        None height
        None x
        None y
    __str__
        test the __str__ function of Rectangle
    area
        test the area function of Rectangle
    display
        Don't know how to test !
    update
        test the update function of Rectangle
    to_dictionary
        test the to_dictionary function of Rectangle
    """

    def setUp(self):
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        pass

    def test_documentation(self):
        """test all documentation of module"""
        # class documentation
        module_class = len(rectangle.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Rectangle.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Rectangle.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Rectangle.width.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Rectangle.height.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Rectangle.x.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Rectangle.y.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Rectangle.area.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Rectangle.display.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Rectangle.__str__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Rectangle.update.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Rectangle.to_dictionary.__doc__)
        self.assertGreater(module_class, 0)

    def test_priority_width_height(self):
        """fuction that test for TypeError"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("str", "str", 3, None)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("str", -2, 3, None)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, -2, 3, None)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, "str", 3, None)

    def test_subclass(self):
        """fuction that test if Rectangle is a subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/rectangle.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )

    def test_valid(self):
        """fuction that test for good assignment of differents value"""
        r1 = Rectangle(10, 2, 34, 121, 45027310974)
        self.assertEqual(r1.id, 45027310974)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 34)
        self.assertEqual(r1.y, 121)

        r2 = Rectangle(10, 2, 5, 65, None)
        self.assertGreater(r2.id, 0)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 65)

        r3 = Rectangle(10, 2)
        self.assertGreater(r3.id, 0)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    # ValueError

    def test_negative_width(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_negative_height(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2)
            r1.width = -10

    def test_negative_x(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1, 2)

    def test_negative_y(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, 4)
            r1.y = -10

    def test_zero_width(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2)
            r1.height = 0

    def test_zero_height2(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 0)

    # TypeError

    def test_too_many_arguments(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_too_few_arguments(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_zero_arguments(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle()

    # string
    def test_string_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle("hello", 2)

    def test_string_height(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, "world")

    def test_string_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "hello", 4)

    def test_string_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "World")

    # float
    def test_float_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1.1, 2)

    def test_float_height(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2.2)

    def test_float_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3.3, 4)

    def test_float_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4.4)

    def test_float_nan_height(self):
        with self.assertRaises(TypeError):
            Rectangle(10, float('nan'), 8, 8)

    def test_float_nan_x(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 10, float('nan'), 8)

    def test_float_nan_y(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 8, float('nan'))

    def test_float_inf_width(self):
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 10, 8, 8)

    def test_float_inf_height(self):
        with self.assertRaises(TypeError):
            Rectangle(10, float('inf'), 8, 8)

    def test_float_inf_x(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 10, float('inf'), 8)

    def test_float_inf_y(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 8, float('inf'))

    def test_float_neg_inf_width(self):
        with self.assertRaises(TypeError):
            Rectangle(float('-inf'), 10, 8, 8)

    def test_float_neg_inf_height(self):
        with self.assertRaises(TypeError):
            Rectangle(10, float('-inf'), 8, 8)

    def test_float_neg_inf_x(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 10, float('-inf'), 8)

    def test_float_neg_inf_y(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 8, float('-inf'))

    # list
    def test_list_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle([1, 1], 2, 3, 4)

    def test_list_height(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, [2, 2], 3, 4)

    def test_list_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, [3, 3], 4)

    def test_list_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, [4, 4])

    # tuple
    def test_tuple_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle((1, 1), 2, 3, 4)

    def test_tuple_height(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, (2, 2), 3, 4)

    def test_tuple_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, (3, 3), 4)

    def test_tuple_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, (4, 4))

    # dict
    def test_dict_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle({"hello": 12}, 2, 3, 4)

    def test_dict_height(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, {"hello": 12}, 3, 4)

    def test_dict_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, {"hello": 12}, 4)

    def test_dict_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, {"hello": 12})

    # Bool :

    def test_Bool_width(self):
        with self.assertRaises(TypeError):
            Rectangle(True, 10, 8, 8)

    def test_Bool_height(self):
        with self.assertRaises(TypeError):
            Rectangle(10, True, 8, 8)

    def test_Bool_x(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 10, True, 8)

    def test_Bool_y(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 8, True)

    # None
    def test_None_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(None, 2, 3, 4)

    def test_None_height(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, None, 3, 4)

    def test_None_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, None, 4)

    def test_None_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, None)

    # __str__

    def test___str__(self):
        """fuction that test for __str__()"""
        r1 = Rectangle(1, 2, 0, 0, 1212121212)
        self.assertEqual(r1.__str__(), "[Rectangle] (1212121212) 0/0 - 1/2")

    # area

    def test_area(self):
        """fuction that test for area()"""
        r1 = Rectangle(12, 43)
        self.assertEqual(r1.area(), 516)

    # display

    def test_diplay(self):
        """Check display func"""
        r1 = Rectangle(8, 7)
        r2 = Rectangle(8, 7, 3, 2, 4)
        with io.StringIO() as buf, redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 8 + "\n") * 7)
        with io.StringIO() as buf, redirect_stdout(buf):
            r2.display()
            output = buf.getvalue()
            self.assertEqual(
                output, (2 * "\n" + (" " * 3 + "#" * 8 + "\n") * 7))

    # update

    def test_update(self):
        """fuction that test for update()"""
        r1 = Rectangle(7, 3, 2, 4)
        r1.update(1234567890, 1, 2, 3, 4)

        self.assertEqual(r1.id, 1234567890)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        r1.update(width=131)
        self.assertEqual(r1.width, 131)
        self.assertEqual(r1.height, 2)

        r1.update(height=454, width=331, y=1)
        self.assertEqual(r1.width, 331)
        self.assertEqual(r1.height, 454)
        self.assertEqual(r1.y, 1)

        r1.update(55, 55, width=50, height=300, id=80)
        self.assertEqual(r1.id, 55)
        self.assertEqual(r1.width, 55)

        r1.update()
        self.assertEqual(r1.height, 454)

    def test_update_error(self):
        """Function to test different error case of uptdate"""
        r1 = Rectangle(7, 3, 2, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(1, "str")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(1, [1, 2])
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(1, -1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(1, 0)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(1, 1, "str")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(1, 1, [1, 2])
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(1, 1, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 1, 1, "str")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 1, 1, [1, 2])
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(1, 1, 1, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 1, 1, 1, "str")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 1, 1, 1, [1, 2])
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(1, 1, 1, 1, -1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(width="str")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(width=[1, 2, 3])
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(width=-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(width=0)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height="str")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height=[1, 2, 3])
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(height=-1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(height=0)
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
        r1 = Rectangle(8, 7, 3, 2, 4)
        self.assertEqual(str(r1), "[Rectangle] (4) 3/2 - 8/7")
        r1.update(4, 3, 2, 1, 0, 2)
        self.assertEqual(str(r1), "[Rectangle] (4) 1/0 - 3/2")

    def test_updateWithoutArg(self):
        """Test update with no arg"""
        r1 = Rectangle(8, 7, 3, 2, 4)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (4) 3/2 - 8/7")

    def test_updateRandomKwarg(self):
        """Test update with random Kwarg"""
        r1 = Rectangle(8, 7, 3, 2, 4)
        r1.update(ThomasLeBoss="oui")
        self.assertEqual(str(r1), "[Rectangle] (4) 3/2 - 8/7")

    # to_dictionary

    def test_to_dictionary(self):
        """fuction that test for to_dictionary()"""
        r1 = Rectangle(1, 2, 3, 4, 1234567890)
        r2 = Rectangle(1, 3, 4, 12, None)
        r3 = Rectangle(1, 3)
        self.assertEqual(
            r1.to_dictionary(),
            {"id": 1234567890, "width": 1, "height": 2, "x": 3, "y": 4},
        )
        self.assertEqual(
            r2.to_dictionary(),
            {"id": 1, "width": 1, "height": 3, "x": 4, "y": 12},
        )
        self.assertEqual(
            r3.to_dictionary(),
            {"id": 2, "width": 1, "height": 3, "x": 0, "y": 0},
        )

    # create

    def test_create(self):
        """Test create a rectangle"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertNotEqual(r1, r2)
        self.assertIsNot(r1, r2)

    # save_to_file | load_from_file || save_to_file_csv | load_form_file_csv

    def test_load_from_file(self):
        r6 = Rectangle(10, 7, 2, 8, 89)
        r7 = Rectangle(2, 4, 0, 0, 90)
        list_rectangles_input = [r6, r7]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        r8 = list_rectangles_output[0]
        r9 = list_rectangles_output[1]
        self.assertIsInstance(r8, Rectangle)
        self.assertIsInstance(r9, Rectangle)
        self.assertIsNot(r6, r8)
        self.assertIsNot(r7, r9)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 10)
        r2 = Rectangle(2, 4, 0, 0, 19)
        filename = r1.__class__.__name__ + ".json"
        s = '[{"x": 2, "y": 8, "id": 10, "height": 7, "width": 10}, '
        s2 = '{"x": 0, "y": 0, "id": 19, "height": 4, "width": 2}]'
        s3 = s + s2
        Rectangle.save_to_file([r1, r2])
        with open(filename, "r") as file:
            f = (file.read())
        self.assertEqual(
            f, s3)
        Rectangle.save_to_file(None)
        with open(filename, "r") as file:
            f = (file.read())
        self.assertEqual(f, '[]')
        Rectangle.save_to_file([])
        with open(filename, "r") as file:
            f = (file.read())
        self.assertEqual(f, '[]')

    def test_saveToFile_loadFromFile(self):
        """Check the both saveto, and loadfrom function to a json file"""
        r1 = Rectangle(1, 2, 3, 4, 1)
        r2 = Rectangle(1, 2, 3, 4, 2)
        listOfRectsInput = [r1, r2]
        Rectangle.save_to_file(listOfRectsInput)
        listOfRectsOutput = Rectangle.load_from_file()
        self.assertEqual(
            listOfRectsInput[0].to_dictionary(
            ), listOfRectsOutput[0].to_dictionary()
        )
        self.assertEqual(
            listOfRectsInput[1].to_dictionary(
            ), listOfRectsOutput[1].to_dictionary()
        )

    def test_saveToFile_loadFromFile_empty(self):
        """Check the both saveto, and loadfrom function to a json file"""
        listOfRectsInput = []
        Rectangle.save_to_file(listOfRectsInput)
        listOfRectsOutput = Rectangle.load_from_file()
        self.assertEqual(
            listOfRectsInput, listOfRectsOutput
        )

    def test_saveToCSV_loadFromCSV(self):
        """Check the both saveto, and loadfrom function to a csv file"""
        r1 = Rectangle(1, 2, 3, 4, 1)
        r2 = Rectangle(1, 2, 3, 4, 2)
        listOfRectsInput = [r1, r2]
        Rectangle.save_to_file_csv(listOfRectsInput)
        listOfRectsOutput = Rectangle.load_from_file_csv()
        self.assertEqual(
            listOfRectsInput[0].to_dictionary(
            ), listOfRectsOutput[0].to_dictionary()
        )
        self.assertEqual(
            listOfRectsInput[1].to_dictionary(
            ), listOfRectsOutput[1].to_dictionary()
        )

    def test_saveToCSV_loadFromCSV_empty(self):
        """Check the both saveto, and loadfrom function to a csv file"""
        listOfRectsInput = []
        Rectangle.save_to_file_csv(listOfRectsInput)
        listOfRectsOutput = Rectangle.load_from_file_csv()
        self.assertEqual(
            listOfRectsInput, listOfRectsOutput
        )


if __name__ == "__main__":
    unittest.main()
