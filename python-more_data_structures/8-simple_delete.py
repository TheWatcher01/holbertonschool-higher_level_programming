#!/usr/bin/python3

"""
def simple_delete(a_dictionary, key=""):

Description:

'simple_delete' function takes a dictionary and a key as arguments.
It deletes the key from the dictionary if it exists.

Arguments:
"a_dictionary" - dictionary of key-value pairs
"key" - key to be deleted from the dictionary

Return:
Function returns 'a_dictionary' after attempting to delete 'key'.
"""


def simple_delete(a_dictionary, key=""):
    # Define function with two parameters: 'a_dictionary' and 'key'.

    a_dictionary.pop(key, None)
    # Delete 'key' from 'a_dictionary' if it exists.
    # If 'key' does not exist, do nothing.

    return a_dictionary
    # Return 'a_dictionary' after attempting to delete 'key'.
