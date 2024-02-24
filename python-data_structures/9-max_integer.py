#!/usr/bin/python3

"""
def max_integer(my_list=[]):

Description:

'max_integer' function takes a list as an argument.
It returns the maximum integer found in the list.
If the list is empty, it returns None.

Arguments:
"my_list" - list of integers

Return:
Function returns maximum integer in list, or None if list is empty.
"""


def max_integer(my_list=[]):
    # Define 'max_integer' with one parameter: 'my_list'.

    if not my_list:
        # If 'my_list' is empty
        return None
        # return None.

    max_value = my_list[0]
    # Initialize 'max_value' with first element of 'my_list'.

    for i in my_list:
        # For each element 'i' in 'my_list'
        if i > max_value:
            # If 'i' is greater than 'max_value'
            max_value = i
            # update 'max_value' with 'i'.

    return max_value
    # Return maximum integer found in 'my_list'.
