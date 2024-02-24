#!/usr/bin/python3

"""
def add_tuple(tuple_a=(), tuple_b=()):

Description:

'add_tuple' function takes two tuples as arguments.
It returns a new tuple where each element is the sum of the elements at the
same index in the input tuples. If an input tuple has less than 2 elements,
it is assumed to be completed with 0s.

Arguments:
"tuple_a" - first tuple of integers
"tuple_b" - second tuple of integers

Return:
Function returns a new tuple with each element being sum of elements
at the same index in the input tuples.
"""


def add_tuple(tuple_a=(), tuple_b=()):
    # Define function with two parameters: 'tuple_a' and 'tuple_b'.

    a = tuple_a + (0, 0)
    # Extend 'tuple_a' with two zeros to ensure it has at least two elements.

    b = tuple_b + (0, 0)
    # Extend 'tuple_b' with two zeros to ensure it has at least two elements.

    return (a[0] + b[0], a[1] + b[1])
    # Return a new tuple where each element is the sum of the elements at
    # same index in 'a' and 'b'.
