#!/usr/bin/python3
"""
This module contains a function to check if an object is an instance of a
class that it inherited from, either directly or indirectly.
"""


def inherits_from(obj, a_class):
    """
    Determine if obj is an instance of a class that it inherited from,
    either directly or indirectly.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if obj is an instance of a class that it inherited from.
        False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
