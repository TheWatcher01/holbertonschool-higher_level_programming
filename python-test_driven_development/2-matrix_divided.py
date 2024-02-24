#!/usr/bin/python3

"""
Module with function that divides all elements of matrix.
"""


def check_matrix(matrix):
    """
    Checks if the matrix is a list of lists of integers/floats.

    Args:
        matrix (list of lists of int/float): Matrix to be checked.

    Raises:
        TypeError: If matrix is not list of lists of integers/floats.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix or [] in matrix:
        raise TypeError(error_msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)
        for elem in row:
            if not isinstance(elem, (int, float)) or isinstance(elem, bool):
                raise TypeError(error_msg)


def check_divisor(div):
    """
    Checks if the divisor is a number and not zero.

    Args:
        div (int/float): The divisor.

    Raises:
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")


def matrix_divided(matrix, div):
    """
    Divides each element of matrix by divisor and rounds result to
    2 decimal places.

    Args:
        matrix (list of lists of int/float): Matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of float: New matrix with each element divided by div.

    Raises:
        TypeError: If matrix is not list of lists of integers/floats,
        or if div is not number.
        ZeroDivisionError: If div is zero.
    """
    check_matrix(matrix)
    check_divisor(div)

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
