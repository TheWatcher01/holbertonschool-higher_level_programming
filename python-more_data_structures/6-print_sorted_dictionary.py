#!/usr/bin/python3

"""
def print_sorted_dictionary(a_dictionary):

Description:

'print_sorted_dictionary' function takes a dictionary as an argument.
It prints the dictionary's keys and their corresponding values in sorted order.

Arguments:
"a_dictionary" - dictionary of key-value pairs

Return:
Function does not return a value. It prints keys and values of 'a_dictionary'.
"""


def print_sorted_dictionary(a_dictionary):
    # Define 'print_sorted_dictionary' with one parameter: 'a_dictionary'.

    [print(f"{key}: {a_dictionary[key]}") for key in sorted(a_dictionary)]
    # For each 'key' in sorted keys of 'a_dictionary',
    # print 'key' and its corresponding value.
