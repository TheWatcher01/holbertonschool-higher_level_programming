#!/usr/bin/python3
"""
Module for MyList class that inherits from list. Adds functionality
to print elements in sorted order without altering the original list.
"""


class MyList(list):
    """
    Inherits from Python's built-in list. Adds method to print
    list elements in sorted (ascending) order.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order. The original
        list order remains unchanged.
        """
        if not all(isinstance(item, int) for item in self):
            raise TypeError("list elements must be integers")
        sorted_list = sorted(self)
        print(sorted(self))  # Sorts and prints list elements
