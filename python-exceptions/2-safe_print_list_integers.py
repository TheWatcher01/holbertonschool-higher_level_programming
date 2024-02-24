#!/usr/bin/python3

"""
def safe_print_list_integers(my_list=[], x=0):

Description:

Function prints 'x' elements of 'my_list' as integers safely.
If 'x' is greater than length of 'my_list', it prints as...
... many elements as possible.
Counts and returns the number of elements printed.
If ValueError or TypeError is raised, it continues to next element.

Arguments:
"my_list" - list of elements
"x" - number of elements to print

Return:
Function returns the number of elements printed.
"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    # Initialize count to 0.

    for i in range(x):
        # Loop over the range of 'x'.

        try:
            print("{:d}".format(my_list[i]), end="")
            # Try to print the element at index 'i' in 'my_list' as an integer.

            count += 1
            # If successful, increment count.

        except (ValueError, TypeError):
            continue
            # If ValueError or TypeError is raised, continue to next element.

    print()
    # Print a newline character at the end.

    return count
    # Return the number of elements printed.
