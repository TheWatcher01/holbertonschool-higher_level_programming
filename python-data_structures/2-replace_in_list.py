#!/usr/bin/python3

"""
def replace_in_list(my_list, idx, element):

Description:

'replace_in_list' function takes a list, an index, and an element as arguments.
It replaces the element at specified index in list with new element.
If index is negative or greater than or equal to length of list,
function returns original list.

Arguments:
"my_list" - list of elements
"idx" - index to replace a specific element in the list
"element" - new element to replace at index

Return:
Function returns modified list after replacing element at specified index,
or original list if index is invalid.
"""


def replace_in_list(my_list, idx, element):
    # Define function with three parameters: 'my_list', 'idx', and 'element'.

    if idx < 0 or idx >= len(my_list):
        # If 'idx' is negative or greater than or equal to length of 'my_list'
        return my_list
        # function returns original list. This indicates that index is invalid

    my_list[idx] = element
    # If 'idx' is valid, replaces element at 'idx' of 'my_list' with 'element'

    return my_list
    # Function returns modified list after replacing element at specified idx
