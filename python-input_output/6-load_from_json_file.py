#!/usr/bin/python3
"""
This module provides functionality to read a JSON file and convert its content
into a Python object. It uses the `json` library for deserialization,
demonstrating a common operation in data serialization processes.

Security Note:
- Path Injection: Unvalidated input in path value creation risks unintended
  file/directory access. To mitigate this, validate the 'filename' parameter
  to ensure it doesn't contain directory traversal sequences or special
  characters. Consider using os.path.abspath and os.path.normpath to resolve
  the absolute path and normalize path separators. Additionally, use
  os.path.basename to extract the filename from a path, which can help prevent
  directory traversal attacks.
- Handle exceptions for non-existent or invalid JSON files.
"""
import json


def load_from_json_file(filename):
    """
    Reads a JSON file and converts it to a Python object.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        The Python object resulting from the JSON file deserialization.

    Security Note:
    - Ensure the filename is validated and points to a safe file location. Be
      wary of directory traversal vulnerabilities. Proper error handling for
      file access and JSON parsing is also important for secure and robust code
    """
    with open(filename, "r", encoding="utf-8") as _file:
        return json.load(_file)
