#!/usr/bin/python3

"""
def print_matrix_integer(matrix=[[]]):

Description:

'print_matrix_integer' function takes a matrix (list of lists) as an argument.
It prints the matrix of integers.

Arguments:
"matrix" - list of lists containing integers

Return:
Function returns None. It prints the matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    # Define function 'print_matrix_integer' with one parameter: 'matrix'.

    for row in matrix:
        # For each list 'row' in 'matrix'
        print(" ".join("{:d}".format(element) for element in row))
        # Use list comprehension to format each integer 'element' in 'row'
        # to a string, join these strings with a space,
        # and print the result.
