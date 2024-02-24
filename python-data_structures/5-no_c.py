#!/usr/bin/python3

"""
def no_c(my_string):

Description:

'no_c' function takes a string as an argument.
It returns a new string where all characters 'c' and 'C' are removed.

Arguments:
"my_string" - string to modify

Return:
Function returns a new string after removing all 'c' and 'C' characters.
"""


def no_c(my_string):
    # Define function 'no_c' with one parameter: 'my_string'.

    return "".join(char for char in my_string if char not in "cC")
    # Use list comprehension to generate a list of characters from 'my_string'
    # that are not 'c' or 'C'.
    # Join these characters into new string and return it.
