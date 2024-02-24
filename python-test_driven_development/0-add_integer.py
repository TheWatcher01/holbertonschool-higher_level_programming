#!/usr/bin/python3
"""

Module contains 'add_integer' function, which adds two numbers together.
It accepts both integers and floats as inputs.
If floats are provided, they are converted to integers before the addition.

"""


def add_integer(a, b=98):
    """
    Adds two numbers, which can be either integers or floats.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)
