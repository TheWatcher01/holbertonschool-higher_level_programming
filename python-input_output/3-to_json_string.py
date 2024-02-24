#!/usr/bin/python3
"""
Module for converting Python objects to JSON strings.

This module contains a function that utilizes the `json` library to convert
Python objects into JSON string representations. This is particularly useful
for serialization of data to a format that can be stored or transmitted and
later reconstructed.
"""

import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON string.

    Uses the `json.dumps` method to serialize `my_obj` to a JSON-formatted
    string. This function is a simple wrapper around `json.dumps`.

    Args:
        my_obj: A Python object to be converted to a JSON string. This can be
                any object that is serializable by `json.dumps`, such as
                dictionaries, lists, strings, etc.

    Returns:
        A JSON string representation of `my_obj`.
    """
    return json.dumps(my_obj)
