#!/usr/bin/python3

"""
def multiply_by_2(a_dictionary):

Description:

'multiply_by_2' function takes a dictionary as an argument.
It creates a new dictionary with the same keys and values multiplied by 2.
This version uses dictionary comprehension for more concise code.

Arguments:
"a_dictionary" - dictionary of key-value pairs

Return:
Function returns a new dictionary with values multiplied by 2.
"""


def multiply_by_2(a_dictionary):
    # Define 'multiply_by_2' with one parameter: 'a_dictionary'.

    return {key: value * 2 for key, value in a_dictionary.items()}
    # Use dictionary comprehension to create new dictionary...
    # ... with values multiplied by 2.
    # For each key-value pair in 'a_dictionary',
    # add the key to new dictionary with value multiplied by 2.
    # Return the new dictionary.
