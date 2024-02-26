#!/usr/bin/python3
"""
Module defines function to append new string after each line containing
specific string in file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends new string after each line containing specific string in a file.

    Args:
        filename (str): Name of the file to be processed.
        search_string (str):
            String to be searched in each line of the file.
        new_string (str):
            String to be appended after each line containing search string.

    Returns:
        None

    Security Note:
    Function does not validate  filename input. This can lead to path injection
    vulnerabilities if filename is taken from untrusted source.
    Always validate and sanitize input to mitigate this risk.
    """
    # Open the file in read write mode
    with open(filename, 'r+') as file:
        # Read all lines in the file and store them in a list
        lines = file.readlines()

        # Move the read/write location to the beginning of the file
        file.seek(0)
        # Remove all content from the file
        file.truncate()

        # Loop through each line in the file
        for line in lines:
            # Write the line back into the file
            file.write(line)

            # If search string is found in line, write new string into file
            if search_string in line:
                # Write the new string into the file
                file.write(new_string)
