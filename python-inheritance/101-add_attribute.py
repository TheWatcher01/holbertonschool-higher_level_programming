#!/usr/bin/python3

"""
This module contains a function to add a new attribute to an object.

Functions:
    add_attribute: Adds a new attribute to an object if it's possible.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to add the attribute to.
        name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attribute.
    """
    # Check if the object can have new attributes.
    # In Python, only objects that are instances of user-defined
    # classes can have new attributes.
    if not hasattr(obj, "__dict__"):
        # If the object can't have new attributes, raise a TypeError.
        raise TypeError("can't add new attribute")
    # If the object can have new attributes, add the attribute.
    setattr(obj, name, value)
