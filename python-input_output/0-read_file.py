#!/usr/bin/python3
"""
This module contains function to read and display contents of specified file.
It demonstrates basic file handling operations in Python, including opening
file with UTF-8 encoding and printing its contents to standard output.
The module adheres to Python 3 standards and best practices.
"""


def read_file(filename=""):
    """
    Function reads and prints the content of a given file.

    Opens file in read mode and uses UTF-8 encoding for compatibility with
    non-ASCII characters.
    If no filename is provided, it defaults to empty string,
    which will result in error upon trying to open file.
    Content of file is then read and printed to the standard output.

    Args:
        filename (str): Path of file to be read. Defaults to an empty string.

    Returns:
        None
    """
    # Open the file in read mode with UTF-8 encoding
    with open(filename, "r", encoding="utf-8") as _file:
        # Read and print file's content without adding new line at end
        print(_file.read(), end="")
