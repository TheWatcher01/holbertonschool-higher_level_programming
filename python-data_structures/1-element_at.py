#!/usr/bin/python3

"""
def element_at(my_list, idx):

Description:

The 'element_at' function takes a list and an index as arguments.
It returns the element at the specified index in the list.
If index is negative or greater than or equal to length of list,
the function returns 'None'.

Arguments:
"my_list" - list of elements
"idx" - index to access a specific element in the list

Return:
Function returns element at specified index in list,
or 'None' if the index is invalid.
"""


def element_at(my_list, idx):
    # Define function 'element_at' with two parameters: 'my_list' and 'idx'.

    if idx < 0 or idx >= len(my_list):
        # If 'idx' is negative or greater than or equal to length of 'my_list'
        return None
        # then function returns 'None'. This indicates that index is invalid.

    return my_list[idx]
    # If 'idx' is negative or greater than or equal to length of 'my_list'
    # function returns element at 'idx' index of 'my_list'.
