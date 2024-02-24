#!/usr/bin/python3
"""
This module contains a function to check if an object is an instance of a
specified class or inherits from it. It's designed for Python 3.
"""


def is_kind_of_class(obj, a_class):
    """
    Determine if obj is an instance of, or inherits from, a_class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if obj is an instance or inherits from a_class; False
        otherwise.
    """
    return isinstance(obj, a_class)
