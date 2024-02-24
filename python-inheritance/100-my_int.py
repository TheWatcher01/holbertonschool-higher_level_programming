#!/usr/bin/python3

"""
This module contains the MyInt class which inherits from int.

Classes:
    MyInt: Represents an integer with inverted == and != operators.
"""


class MyInt(int):
    """
    Represents an integer with inverted == and != operators.
    Inherits from int.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other (int): The integer to compare with.

        Returns:
            bool: True if self and other are not equal, False otherwise.
        """
        # Use the != operator from the parent class (int)
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other (int): The integer to compare with.

        Returns:
            bool: True if self and other are equal, False otherwise.
        """
        # Use the == operator from the parent class (int)
        return super().__eq__(other)
