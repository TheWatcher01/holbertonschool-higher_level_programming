#!/usr/bin/python3
import io
from contextlib import redirect_stdout
import sys
from models.rectangle import Rectangle
import unittest
import os


class TestRectangle(unittest.TestCase):

    def test_01_rectangle_creation(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_02_rectangle_creation_with_x_y(self):
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.x, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.y, 4)

    def test_03_rectangle_creation_with_id(self):
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)

    def test_04_rectangle_creation_string_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_05_rectangle_creation_string_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_06_rectangle_creation_string_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_07_rectangle_creation_string_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_08_rectangle_creation_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_09_rectangle_creation_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_10_rectangle_creation_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_11_rectangle_creation_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_12_rectangle_creation_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_13_rectangle_creation_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_14_rectangle_str_method(self):
        r5 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r5.__str__(), '[Rectangle] (5) 3/4 - 1/2')

    def test_15_rectangle_display_method(self):
        pass

    def test_16_rectangle_to_dictionary_method(self):
        r6 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r6.to_dictionary(), {
                         'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_17_rectangle_update_method(self):
        r7 = Rectangle(1, 2, 3, 4, 5)
        r7.update(6, 7, 8, 9, 10)
        self.assertEqual(r7.__str__(), '[Rectangle] (6) 9/10 - 7/8')

    def test_18_rectangle_to_dictionary(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dict = r1.to_dictionary()
        self.assertEqual(
            r1_dict, {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8})

    def test_19_rectangle_update_args(self):
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(89)
        self.assertEqual(r1.id, 89)

    def test_20_rectangle_update_args_more(self):
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_21_rectangle_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(height=1, width=2, x=3, y=4, id=89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_22_rectangle_create(self):
        r1 = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_23_rectangle_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_24_rectangle_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_25_rectangle_save_to_file_one_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                file.read(), '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_26_rectangle_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_27_rectangle_load_from_file_exists(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].to_dictionary(), r1.to_dictionary())

    def test_27_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(**{'id': 89})
        self.assertEqual(r1.id, 89)

    def test_28_update_kwargs_more(self):
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(**{'id': 89, 'width': 1})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_29_update_kwargs_full(self):
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_30_create(self):
        r1 = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_31_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_32_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_33_save_to_file_single(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            self.assertNotEqual(file.read(), "[]")

    def test_34_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_35_load_from_file_with_file(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1])
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].id, r1.id)

    def test_36_valid_width(self):
        r1 = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r1.width = "10"

    def test_37_valid_height(self):
        r1 = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r1.height = "10"

    def test_38_valid_x(self):
        r1 = Rectangle(1, 2, 3)
        with self.assertRaises(TypeError):
            r1.x = "10"

    def test_39_valid_y(self):
        r1 = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r1.y = "10"

    def test_40_valid_width_negative(self):
        r1 = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r1.width = -10

    def test_41_valid_height_negative(self):
        r1 = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r1.height = -10


    def test_display_without_x_and_y(self):
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_display_without_y(self):
        r = Rectangle(2, 2, 2)
        expected_output = "  ##\n  ##\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_area_exists(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        r = Rectangle(2, 2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            self.assertEqual(buf.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
