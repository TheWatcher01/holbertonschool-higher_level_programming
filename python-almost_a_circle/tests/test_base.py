#!/usr/bin/python3
'''Module for Base unit tests.'''
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import unittest
import json
import os





class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def test_initialisation(self):
        """Tests Base() instantiation."""
        b = Base()
        self.assertGreater(b.id, 0)

    def test_incrementation(self):
        """Test Base() incrementation"""
        a = Base()
        b = Base()
        self.assertEqual(b.id, a.id + 1)

    def test_saving_id(self):
        """Test Base(89)"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Args is None"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_empty_list(self):
        """Empty list"""
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_id(self):
        """List contains [ { 'id': 12 }]"""
        input_data = [{'id': 12}]
        expected_output = json.dumps(input_data)
        json_dictionary = Base.to_json_string(input_data)
        self.assertEqual(json_dictionary, expected_output)

    def test_from_json_string_none(self):
        """Args is None"""
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_from_json_string_empty_list(self):
        """Test for "[]"."""
        list_output = Base.from_json_string("[]")
        self.assertEqual(list_output, [])

    def test_from_json_string_id(self):
        """List contains [ { 'id': 89 }]"""
        input_data = '[ { "id": 89 }]'
        expected_output = [{'id': 89}]
        json_dictionary = Base.from_json_string(input_data)
        self.assertEqual(json_dictionary, expected_output)

    def test_create_1(self):
        """Test create with a dict : **{ 'id': 89 }"""
        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(r1.id, 89)

    def test_create_2(self):
        """Test create with a dict : **{ 'id': 89, 'width': 1 }"""
        r1 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create_3(self):
        """Test create with a dict : **{ 'id': 89, 'width': 1, 'height': 2 }"""
        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_create_4(self):
        """Test create with a dict : **{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }"""
        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_create_5(self):
        """Test create with a dict : **{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }"""
        r1 = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_create_6(self):
        """Test create with a dict : **{ 'id': 89, 'size': 1 }"""
        s1 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

    def test_create_7(self):
        """Test create with a dict : **{ 'id': 89, 'size': 1, 'x': 2 }"""
        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

    def test_create_8(self):
        """Test create with a dict : **{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }"""
        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def setUp(self):
        """Set up for the tests."""
        Base._Base__nb_objects = 0
        self.filepath = "Base.json"

    def tearDown(self):
        """Tear down for the tests."""
        if os.path.exists(self.filepath):
            os.remove(self.filepath)


if __name__ == "__main__":
    unittest.main()
