#!/usr/bin/python3

"""
def only_diff_elements(set_1, set_2):

Description:

'only_diff_elements' function takes two sets as arguments.
It returns a new set with the elements present in only one of the sets.
This is achieved by using symmetric difference operator '^' on two sets.

Arguments:
"set_1" - first set of elements
"set_2" - second set of elements

Return:
A set with elements present in only one of 'set_1' and 'set_2'.
"""


def only_diff_elements(set_1, set_2):
    # Define 'only_diff_elements' with two parameters: 'set_1' and 'set_2'.
    # Use the symmetric difference operator '^' to find elements...
    # ... present in only one of 'set_1' and 'set_2'.

    return set_1 ^ set_2
    # Return the set with elements present in only one of 'set_1' and 'set_2'.
