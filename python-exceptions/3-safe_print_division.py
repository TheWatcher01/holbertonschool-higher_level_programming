#!/usr/bin/python3

"""
def safe_print_division(a, b):

Description:

Function divides 'a' by 'b' and prints result safely.
If 'b' is zero, it prints 'None' and returns 'None'.
If division is successful, it prints and returns result.

Arguments:
"a" - dividend
"b" - divisor

Return:
Function returns result of division or 'None' if division by zero.
"""


def safe_print_division(a, b):
    result = None
    # Initialize result to None.

    try:
        # Try block to attempt division.
        result = a / b
        # Attempt to divide 'a' by 'b'.

    except ZeroDivisionError:
        # Except block to handle ZeroDivisionError.
        pass
        # If ZeroDivisionError is raised, pass and continue.

    finally:
        # Finally block to execute regardless of try-except outcome.
        print("Inside result: {}".format(result))
        # Print result.

        return result
        # Return result of division or 'None' if division by zero.
