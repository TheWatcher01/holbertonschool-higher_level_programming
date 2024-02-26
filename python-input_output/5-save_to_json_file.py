#!/usr/bin/python3
"""
Module provides functionality to serialize Python object into JSON string
and write it to file. It uses `json` library for serialization.

Security Note:
- Ensure that object to be serialized and filename do not contain sensitive
  information.
- Validate inputs to avoid serialization of unexpected or malicious
  data and to preventnpath traversal vulnerabilities with the filename.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Serialize Python object and save it as JSON string in a file.

    Function opens file in write mode and uses `json.dumps` to serialize
    Python object (`my_obj`) into JSON-formatted string. It then writes
    this string to specified file. Function does not return value.

    Args:
        my_obj: Python object to serialize. It can be any object that is
                serializable by `json.dumps`, such as dictionaries, lists, etc.
        filename (str): Path of the file where the JSON string will be saved.

    Security Note:
    - Be cautious of serializing sensitive information.
    - Validate `filename` to ensure it is safe path to avoid file system attack
    """
    with open(filename, "w", encoding="utf-8") as _file:
        _file.write(json.dumps(my_obj))
