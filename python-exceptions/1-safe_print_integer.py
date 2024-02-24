#!/usr/bin/python3

"""
def safe_print_integer(value):

Description:

Function tries to print 'value' as an integer.
If successful, it returns True.
If a ValueError is raised, it returns False.

Arguments:
"value" - value to print

Return:
Function returns True if 'value' was printed successfully, False otherwise.
"""


def safe_print_integer(value):
    try:
        # Try to print 'value' as an integer.
        print("{:d}".format(value))
        # If successful, return True.
        return True
    except (ValueError, TypeError):
        # If ValueError or TypeError is raised, return False.
        return False
