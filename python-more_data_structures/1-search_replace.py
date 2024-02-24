#!/usr/bin/python3

"""
def search_replace(my_list, search, replace):

Description:

Function takes a list, a search element, and a replace element.
Returns new list where all occurrences of 'search' are replaced by 'replace'.

Arguments:
"my_list" - list of elements
"search" - element to be replaced
"replace" - new element

Return:
Function returns a new list with 'search' replaced by 'replace'.
"""


def search_replace(my_list, search, replace):
    # Define function with three parameters.

    return [replace if element == search else element for element in my_list]
    # Return new list with 'search' replaced by 'replace' in 'my_list'.
