#!/usr/bin/python3

"""
def update_dictionary(a_dictionary, key, value):

Description:

Function takes a dictionary, a key, and a value as arguments.
It updates dictionary with provided key-value pair. If key already exists,
value is updated. If key does not exist, it is added to the dictionary.

Arguments:
"a_dictionary" - dictionary of key-value pairs
"key" - key to be added or updated in the dictionary
"value" - value corresponding to the key

Return:
Function returns updated 'a_dictionary'.
"""


def update_dictionary(a_dictionary, key, value):
    # Define function with parameters: 'a_dictionary', 'key', and 'value'.

    a_dictionary[key] = value
    # Add 'key'-'value' pair to 'a_dictionary' or update if 'key' already exist

    return a_dictionary
    # Return updated 'a_dictionary'.
