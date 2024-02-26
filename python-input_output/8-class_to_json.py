#!/usr/bin/python3
"""
Module provides function to convert class instance attributes to dictionary.
"""


def class_to_json(obj):
    """
    Converts the attributes of a class instance into a dictionary.

    Args:
        obj (Any): The class instance to be converted into a dictionary.

    Returns:
        dict: A dictionary containing the attributes of the class instance.
    """
    attributes = vars(obj)  # Extract the attributes of the class instance
    return attributes  # Return the attributes as a dictionary
