#!/usr/bin/python3

"""
Module that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Print the full name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    error_msg1 = "first_name must be a string"
    error_msg2 = "last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError(error_msg1)

    if last_name is None:
        last_name = ""
    elif not isinstance(last_name, str):
        raise TypeError(error_msg2)

    first_name_esc = first_name.encode('unicode_escape').decode()
    last_name_esc = last_name.encode('unicode_escape').decode()
    print(f"My name is {first_name_esc} {last_name_esc}")
