#!/usr/bin/python3

"""
def print_reversed_list_integer(my_list=[]):

Description:

'print_reversed_list_integer' function takes a list as an argument.
It prints all integers in list in reverse order.
If list is empty, function does nothing.

Arguments:
"my_list" - list of integers

Return:
Function returns None. It prints elements of list in reverse order.
"""


def print_reversed_list_integer(my_list=[]):
    # Define 'print_reversed_list_integer' with one parameter: 'my_list'.

    my_list.reverse()
    # Reverse order of elements in 'my_list'.

    for i in my_list:
        # For each element 'i' in 'my_list'
        print("{:d}".format(i))
        # print 'i' in decimal format.

    # Function does not return. It prints elements of list in reverse order.
