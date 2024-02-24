#!/usr/bin/python3
"""
Module for the 'Lookup' task of the Python - Inheritance project.

Module defines one function, lookup(), which is used to list all available
attributes and methods of an object. Function is implemented without
importing any external modules.
"""


def lookup(obj):
    """
    Return list of available attributes and methods of an object.

    Function uses built-in dir() method to return a list of valid
    attributes and methods of passed object. It is useful for introspection
    to understand what operations can be performed on the object.

    Args:
        obj (Any): The object for introspection.

    Returns:
        list: A list of string names of the object's attributes and methods.
    """
    return dir(obj)
