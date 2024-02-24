#!/usr/bin/python3

"""
def delete_at(my_list=[], idx=0):

Description:

'delete_at' function takes a list and an index as arguments.
It deletes the element at the specified index in the list.
If index is negative or greater than or equal to length of list,
the function returns the original list without any modification.

Arguments:
"my_list" - list of elements
"idx" - index to delete a specific element in the list

Return:
Function returns modified list after deleting element at specified index,
or the original list if index is invalid.
"""


def delete_at(my_list=[], idx=0):
    # Define function 'delete_at' with two parameters.

    if idx < 0 or idx >= len(my_list):
        # If 'idx' is negative or greater than or equal to length of 'my_list'
        return my_list
        # then function returns original list.
        # This indicates that index is invalid.

    del my_list[idx]
    # If 'idx' is valid, function deletes element at 'idx' index of 'my_list'.

    return my_list
    # Function returns modified list after deleting element at specified index.
