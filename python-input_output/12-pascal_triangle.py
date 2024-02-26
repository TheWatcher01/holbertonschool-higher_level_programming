#!/usr/bin/python3
"""
Module defines function to generate Pascal's triangle up to
specified number of rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows in the triangle to generate.

    Returns:
        list: List of lists, where each inner list represents row of
        Pascal's triangle.
    """
    if n <= 0:
        return []  # Return an empty list for non-positive input

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each row with a 1
        last_row = triangle[i - 1]  # Get last row to calculate the current row

        # Calculate the values for the current row based on the last row
        for j in range(1, i):
            row.append(last_row[j - 1] + last_row[j])

        row.append(1)  # End each row with a 1
        triangle.append(row)  # Add the current row to the triangle

    return triangle  # Return the completed Pascal's triangle
