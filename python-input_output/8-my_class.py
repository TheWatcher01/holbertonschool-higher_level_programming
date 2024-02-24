#!/usr/bin/python3
"""
This module defines the MyClass class.
"""


class MyClass:
    """
    A simple MyClass.

    Attributes:
        name (str): The name of the class instance.
        number (int): Number associated with class instance, initialized to 0.
    """

    def __init__(self, name):
        """
        The constructor for MyClass.

        Args:
            name (str): The name to be assigned to the instance.
        """
        self.name = name  # Assign the name to the instance
        self.number = 0   # Initialize number to 0

    def __str__(self):
        """
        String representation of the MyClass instance.

        Returns:
            str: A formatted string representing the MyClass instance.
        """
        return "[MyClass] {} - {:d}".format(self.name, self.number)
