#!/usr/bin/python3

"""
def best_score(a_dictionary):

Description:

'best_score' function takes a dictionary as an argument.
It returns key with highest value. If dictionary is empty or None,
it returns None.

Arguments:
"a_dictionary" - dictionary of key-value pairs

Return:
Function returns key with highest value in 'a_dictionary'
or None if 'a_dictionary' is empty or None.
"""


def best_score(a_dictionary):
    # Define 'best_score' with one parameter: 'a_dictionary'.

    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
    # If 'a_dictionary' is not empty or None, return key with highest value.
    # Use 'get' method of dictionary to retrieve value for each key.
    # 'max' function returns key with highest value.
    # If 'a_dictionary' is empty or None, return None.
