#!/usr/bin/python3

"""
This module contains the Square class which inherits from Rectangle.
"""

# Import the Rectangle class from the 9-rectangle module.
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square. Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with validated size.

        Args:
            size (int): The size of the square.
        """
        # Validate size using integer_validator method from parent class.
        self.integer_validator("size", size)

        # Call constructor of parent class (Rectangle) with size as both
        # width and height.
        super().__init__(size, size)

        # Set the private attribute __size.
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        # Calculate and return the area of the square.
        return self.__size ** 2

    def __str__(self):
        """
        Returns the print() and str() representation of a Square instance.
        """
        # Return a string representation of the square.
        return f"[Square] {self.__size}/{self.__size}"
