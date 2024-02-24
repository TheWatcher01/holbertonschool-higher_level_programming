#!/usr/bin/python3

"""
def safe_print_list(my_list=[], x=0):

Description:

Function prints 'x' elements of 'my_list' safely.
If x is greater than length of 'my_list', it print as many element as possible
Counts and returns number of elements printed.

Arguments:
"my_list" - list of elements
"x" - number of elements to print

Return:
Function returns number of elements printed.
"""


def safe_print_list(my_list=[], x=0):
    # Initialize counter to 0.
    counter = 0

    # Loop over range of 'x'.
    for i in range(x):
        try:
            # Try to print element at index 'i' in 'my_list'.
            print(my_list[i], end="")
            # If successful, increment counter.
            counter += 1
        except IndexError:
            # If IndexError is raised, pass and continue.
            pass

    # Print newline character at end.
    print()

    # Return number of elements printed.
    return counter
