#!/usr/bin/python3
"""
This module implements the LockedClass.

LockedClass is a simple demonstration of using __slots__ in Python.
It's designed to restrict creation of instance attributes to just 'first_name'.
Class can be used to understand concept of limiting instance attributes for
memory optimization in Python.

Typical usage example:

    my_object = LockedClass()
    my_object.first_name = "John"
    # The following will raise an AttributeError
    # my_object.last_name = "Snow"
"""


class LockedClass:
    """
    LockedClass limits attribute creation to only 'first_name'.
    Prevents creation of any new instance attributes apart from 'first_name'.
    """

    __slots__ = ['first_name']

    def __init__(self):
        """
        Initializes the LockedClass instance.
        """
        pass
