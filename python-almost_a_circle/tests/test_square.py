#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.square import Square
import json


class TestSquare(unittest.TestCase):

    def test_square_create(self):
        s = Square.create(**{'id': 89})
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)

    def test_square_create_size(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_square_create_x(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_square_create_y(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_creation(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_creation_with_x(self):
        s = Square(1, 2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_square_creation_with_x_y(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_creation_with_string(self):
        with self.assertRaises(TypeError):
            s = Square("1")

    def test_square_creation_with_negative(self):
        with self.assertRaises(ValueError):
            s = Square(-1)

    def test_square_creation_with_zero(self):
        with self.assertRaises(ValueError):
            s = Square(0)

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(json.dumps([obj.to_dictionary()
                           for obj in list_objs]))

    def test_save_to_file(self):
        Square._Square__nb_objects = 0  # Reset count instances
        s = Square(1)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + ".json", "r") as file:
                return [cls.create(**d) for d in json.load(file)]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    def test_load_from_file_nonexistent(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_initialisation(self):
        s1 = Square(1)
        self.assertIsInstance(s1, Square)
        self.assertEqual(s1.size, 1)

        s2 = Square(1, 2)
        self.assertIsInstance(s2, Square)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)

        s3 = Square(1, 2, 3)
        self.assertIsInstance(s3, Square)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)

        with self.assertRaises(TypeError):
            s4 = Square("1")

        with self.assertRaises(TypeError):
            s5 = Square(1, "2")

        with self.assertRaises(TypeError):
            s6 = Square(1, 2, "3")

        s7 = Square(1, 2, 3, 4)
        self.assertIsInstance(s7, Square)
        self.assertEqual(s7.size, 1)
        self.assertEqual(s7.x, 2)
        self.assertEqual(s7.y, 3)
        self.assertEqual(s7.id, 4)

        with self.assertRaises(ValueError):
            s8 = Square(-1)

        with self.assertRaises(ValueError):
            s9 = Square(1, -2)

        with self.assertRaises(ValueError):
            s10 = Square(1, 2, -3)

        with self.assertRaises(ValueError):
            s11 = Square(0)

    def test__str__(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.to_dictionary(), {
                         'id': 4, 'size': 1, 'x': 2, 'y': 3})

    def test_update_1(self):
        Base._Base__nb_objects = 0
        s1 = Square(1, 2, 3, 4)
        s1.update()
        self.assertEqual(str(s1), "[Square] (4) 2/3 - 1")

    def test_update_2(self):
        Base._Base__nb_objects = 0
        s1 = Square(1, 2, 3, 4)
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 2/3 - 1")

    def test_update_3(self):
        Base._Base__nb_objects = 0
        s1 = Square(1, 2, 3, 4)
        s1.update(89, 1)
        self.assertEqual(str(s1), "[Square] (89) 2/3 - 1")

    def test_update_4(self):
        Base._Base__nb_objects = 0
        s1 = Square(1, 2, 3, 4)
        s1.update(89, 1, 2)
        self.assertEqual(str(s1), "[Square] (89) 2/3 - 1")

    def test_update_5(self):
        Base._Base__nb_objects = 0
        s1 = Square(1, 2, 3, 4)
        s1.update(89, 1, 2, 3)
        self.assertEqual(str(s1), "[Square] (89) 2/3 - 1")

    def test_update_with_dict_1(self):
        s1 = Square(1, 2, 3, 4)
        s1.update(**{'id': 89})
        self.assertEqual(s1.id, 89)

    def test_update_with_dict_2(self):
        s1 = Square(1, 2, 3, 4)
        s1.update(**{'id': 89, 'size': 1})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

    def test_update_with_dict_3(self):
        s1 = Square(1, 2, 3, 4)
        s1.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

    def test_update_with_dict_4(self):
        s1 = Square(1, 2, 3, 4)
        s1.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)


    def test_save_to_file_none(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        Square.save_to_file(None)

        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_single_square(self):
        s = Square(1)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            self.assertNotEqual(file.read(), "[]")


if __name__ == "__main__":
    unittest.main()
