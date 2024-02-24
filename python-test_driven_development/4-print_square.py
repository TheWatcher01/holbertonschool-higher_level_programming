#!/usr/bin/python3

"""
Module that prints a square with the character #.
"""


def print_square(size):
    """
    Print a square with the character #.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    int_error_msg = "size must be an integer"
    value_error_msg = "size must be >= 0"

    if isinstance(size, float) and size.is_integer():
        size = int(size)
    elif not isinstance(size, int):
        raise TypeError(int_error_msg)

    if size < 0:
        raise ValueError(value_error_msg)

    for _ in range(size):
        print("#" * size)
