#!/usr/bin/python3

"""
Module defines Square class that initializes square of given size.
"""


class Square:
    """
    Square class. Class is used to create square of given size.

    Attributes:
        __size (int): Size of square, defaults to 0.
    """

    def __init__(self, size=0):
        """
        Constructor of Square class.

        Args:
            size (int, optional): Size of square to be created. Defaults to 0.
        """
        self.size = size  # Set size of square.

    @property
    def size(self):
        """
        Getter for size attribute.

        Returns:
            int: Size of square.
        """
        # Return size of square.
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.

        Args:
            value (int): New size of square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        # Check if value is an integer.
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # Check if value is greater than or equal to 0.
        if value < 0:
            raise ValueError("size must be >= 0")
        # Set new size of square.
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        # Calculate and return the area of the square.
        return self.__size * self.__size

    def my_print(self):
        """
        Print a square of '#' characters of the size of the square.
        If the size is 0, print an empty line.
        """
        # Check if size is 0.
        if self.__size == 0:
            print()  # Print an empty line.
        else:
            # Print a square of '#' characters of the size of the square.
            for _ in range(self.__size):
                print("#" * self.__size)
