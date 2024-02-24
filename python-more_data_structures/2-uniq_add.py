#!/usr/bin/python3

"""
def uniq_add(my_list=[]):

Description:

'uniq_add' function takes a list as an argument.
It returns the sum of unique elements in the list.
This is achieved by converting the list to a set...
... (which removes duplicates) and then summing the elements.

Arguments:
"my_list" - list of integers

Return:
Function returns sum of unique integers in list.
"""


def uniq_add(my_list=[]):
    # Define 'uniq_add' with one parameter: 'my_list'.

    return sum(set(my_list))
    # Convert 'my_list' to a set to remove duplicates.
    # Use 'sum' function to add up the unique elements.
    # Return the sum of unique elements in 'my_list'.
