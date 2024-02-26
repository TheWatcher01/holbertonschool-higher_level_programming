#!/usr/bin/python3
"""
Module provides functionality to write text to specified file.
It includes function to write given text to file, supporting UTF-8 encoding,
which ensures compatibility with wide range of characters beyond ASCII.

Security Note:
Function has potential security vulnerability known as Path Traversal or
Directory Traversal. Function does not validate filename input which
could allow an attacker to read or write to arbitrary files on system by
providing a filename with a relative path (e.g., '../../etc/passwd').
To mitigate this risk, it is recommended to validate the filename input,
ensuring it does not contain path traversal sequences or special characters.
One way to do this is by importing the 'os' module and using the
'os.path.basename(filename)' function to get the base name of the file,
ignoring any directory paths.
"""


def write_file(filename="", text=""):
    """
    Writes text to a specified file.

    Function opens file in write mode. If file does not exist, it will
    be created. If no filename is specified, it defaults to empty string, which
    will lead to error. The text is written to file using UTF-8 encoding.

    Args:
        filename (str): Path file to be written to. Defaults to empty string.
        text (str): Text to be written to file. Defaults to empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as _file:
        return _file.write(text)
