#!/usr/bin/python3
"""
Module provides functionality to append text to specified file.
Includes function for appending given text to file, supporting UTF-8 encoding,
essential for compatibility with wide range of characters beyond ASCII.

Security Note:
Function has potential security vulnerability known as Path Traversal or
Directory Traversal. Function does not validate filename input which
could allow attacker to append to arbitrary files on system by
providing filename with relative path (e.g., '../../etc/passwd').
To mitigate this risk, recommended to validate filename input,
ensuring it does not contain path traversal sequences or special characters.
One way to do this is by importing 'os' module and using
'os.path.basename(filename)' function to get base name of file,
ignoring any directory paths.
"""


def append_write(filename="", text=""):
    """
    Appends text to specified file.
    Function opens file in append mode. If file does not exist, it will
    be created. Then appends provided text to file using UTF-8 encoding.
    Function returns number of characters written.

    Args:
        filename (str): Path file to be appended to. Defaults to empty string.
        text (str): Text to be appended to file. Defaults to empty string.

    Returns:
        int: Number of characters appended to file.
    """
    with open(filename, "a", encoding="utf-8") as _file:
        return _file.write(text)
