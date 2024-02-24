#!/usr/bin/python3

"""Unittest for the max_integer([..]) function
"""

# Import unittest module.
import unittest

# Import the `max_integer` function from the module '6-max_integer'
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A test class for the 'max_integer' function.

    Defines serie of test case to validate behavior of 'max_integer' function.
    It include test for basic functionality, handling of various input scenario
    and error case.
    """

    def test_max_in_order(self):
        # Test with numbers in ascending order
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_not_in_order(self):
        # Test with numbers not in order
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_in_reverse_order(self):
        # Test with numbers in descending order
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_same_numbers(self):
        # Test with same numbers
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_max_with_negative(self):
        # Test with negative and positive numbers
        self.assertEqual(max_integer([2, 3, -1]), 3)

    def test_max_all_negative(self):
        # Test with all numbers negative
        self.assertEqual(max_integer([-2, -3, -1]), -1)

    def test_max_single_element(self):
        # Test with single element
        self.assertEqual(max_integer([1]), 1)

    def test_max_empty_list(self):
        # Test with empty list
        self.assertEqual(max_integer([]), None)

    def test_max_no_argument(self):
        # Test with no argument
        self.assertEqual(max_integer(), None)
