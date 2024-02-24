#!/usr/bin/python3

"""
Module contains 'text_indentation' function, which prints text with 2 new lines
after each of these characters: '.', '?', and ':'.
Function ensures there is no space at beginning or at end of each printed line.
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.

    Function iterates through each character in text.
    If character is '.', '?', or ':',
    it prints character followed by two new lines.
    Otherwise, it prints the character as is.
    Spaces at beginning or end of each printed line are removed.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line_chars = ['.', '?', ':']
    line = ""
    for char in text:
        if char == ' ' and (not line or line[-1] == '\n'):
            continue
        line += char
        if char in new_line_chars:
            print(line, end="\n\n")
            line = ""
    if line:
        print(line, end="")
