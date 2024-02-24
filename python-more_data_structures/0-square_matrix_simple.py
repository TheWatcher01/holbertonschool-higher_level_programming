#!/usr/bin/python3

"""
def square_matrix_simple(matrix=[]):

Description:

'square_matrix_simple' function takes a matrix as an argument.
It returns a new matrix with the square of each element of the original matrix.

Arguments:
"matrix" - list of lists of integers

Return:
Function returns a new matrix with the square of each element.
"""


def square_matrix_simple(matrix=[]):
    # Define 'square_matrix_simple' with one parameter: 'matrix'.

    return [[element**2 for element in row] for row in matrix]
    # Return a new matrix where each element is the square of the corresponding
    # element in the original 'matrix'.
