#!/usr/bin/python3

"""
def print_list_integer(my_list=[]):

Description:

The 'print_list_integer' function takes a list as an argument.
It prints each element in the list on a new line.
The list is assumed to contain only integers.

Arguments:
"my_list" - list of integers

Return:
This function does not return anything.
"""


def print_list_integer(my_list=[]):
    # Define function 'print_list_integer' with one parameter: 'my_list'.
    for i in my_list:
        # For each element 'i' in 'my_list'...
        print("{:d}".format(i))
        # ...print 'i' as an integer.
