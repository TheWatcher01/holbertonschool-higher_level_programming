#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_01_id_auto_assign(self):
        """Test automatic ID assignment."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_02_id_auto_increment(self):
        """Test automatic ID increment."""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_03_id_manual_assign(self):
        """Test manual ID assignment."""
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_04_to_json_string_None(self):
        """Test JSON string of None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_05_to_json_string_empty_list(self):
        """Test JSON string of an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_06_to_json_string_list(self):
        """Test JSON string of a list."""
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_07_to_json_string_return_type(self):
        """Test return type of to_json_string method."""
        self.assertIsInstance(Base.to_json_string([{'id': 12}]), str)

    def test_08_from_json_string_None(self):
        """Test creating from JSON string None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_09_from_json_string_empty_str(self):
        """Test creating from empty JSON string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_10_from_json_string_valid_str(self):
        """Test creating from valid JSON string."""
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])

    def test_11_from_json_string_return_type(self):
        """Test return type of from_json_string method."""
        self.assertIsInstance(Base.from_json_string('[{"id": 89}]'), list)


if __name__ == "__main__":
    unittest.main()
