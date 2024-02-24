#!/usr/bin/python3

"""
def divisible_by_2(my_list=[]):

Description:

'divisible_by_2' function takes a list as an argument.
It returns new list with boolean values. Each boolean value indicates whether
the corresponding element in the input list is divisible by 2.

Arguments:
"my_list" - list of integers

Return:
Function returns a new list with boolean values. True if corresponding
element in 'my_list' is divisible by 2, False otherwise.
"""


def divisible_by_2(my_list=[]):
    # Define function 'divisible_by_2' with one parameter: 'my_list'.

    return [i % 2 == 0 for i in my_list]
    # Use list comprehension to generate a new list.
    # For each element 'i' in 'my_list', check if 'i' is divisible
    # by 2 (i.e., 'i' modulo 2 equals 0). If so, append True
    # to the new list; otherwise, append False.
