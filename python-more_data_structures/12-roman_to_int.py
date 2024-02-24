#!/usr/bin/python3

"""
def roman_to_int(roman_string):

Description:

'roman_to_int' function takes a string representing a Roman numeral.
It converts Roman numeral to an integer.
If input is not a string or is None, function returns 0.

Arguments:
"roman_string" - string representing a Roman numeral

Return:
Function returns integer equivalent of 'roman_string'.
"""


def roman_to_int(roman_string):
    # Define 'roman_to_int' with one parameter: 'roman_string'.

    if not isinstance(roman_string, str) or roman_string is None:
        # If 'roman_string' is not a string or is None, return 0.
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    # Define dictionary 'roman_dict' to map Roman numerals to integer values.

    total = 0
    # Init 'total' to 0. This will hold integer equivalent of 'roman_string'.

    for i in range(len(roman_string) - 1, -1, -1):
        # Iterate over 'roman_string' in reverse order.

        if i == len(roman_string) - 1 or \
           roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]]:
            total += roman_dict[roman_string[i]]
        # If current Roman numeral is greater than or equal to next
        # one (to right), add its value to 'total'.

        else:
            total -= roman_dict[roman_string[i]]
            # If current Roman numeral is less than next one,
            # subtract its value from 'total'.

    return total
    # Return integer equivalent of 'roman_string'.
