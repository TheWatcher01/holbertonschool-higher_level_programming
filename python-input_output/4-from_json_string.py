#!/usr/bin/python3
"""
Module provides function to convert JSON string back into Python object.
It utilizes `json` library for conversion, demonstrating common operation
in data serialization and deserialization processes.
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string into a Python object.

    Utilizes `json.loads` method to deserialize JSON string (`my_str`) into
    Python object. Function is particularly useful for converting JSON strings,
    often used in data transmission, back into Python-readable format.

    Args:
        my_str (str): String in JSON format to be converted into Python object.

    Returns:
        The Python object resulting from the JSON string deserialization.
    """
    return json.loads(my_str)
