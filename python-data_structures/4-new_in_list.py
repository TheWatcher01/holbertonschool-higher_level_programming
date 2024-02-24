#!/usr/bin/python3

"""
def new_in_list(my_list, idx, element):

Description:

'new_in_list' function takes a list, an index, and an element as arguments.
It creates a new list, replaces the element at specified index in new list
with new element. If index is negative or greater than or equal to length of
list, function returns the new list without any modification.

Arguments:
"my_list" - list of elements
"idx" - index to replace a specific element in the list
"element" - new element to replace at index

Return:
Function returns a new list after replacing element at specified index,
or new list without any modification if index is invalid.
"""


def new_in_list(my_list, idx, element):
    # Define function with three parameters: 'my_list','idx', and 'element'

    new_list = my_list.copy()
    # Create a copy of 'my_list' and assign it to 'new_list'.

    if idx >= 0 and idx < len(new_list):
        # If 'idx' is non-negative and less than length of 'new_list'
        new_list[idx] = element
        # function replaces element at 'idx' of 'new_list' with 'element'.

    return new_list
    # Function returns 'new_list' after replacing element at specified index,
    # or 'new_list' without any modification if index is invalid.
