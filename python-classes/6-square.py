#!/usr/bin/python3

"""
This module defines a class Square with private instance attributes size and
position. It includes methods to calculate the area of the square and to print
the square using the '#' character.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes:
        __size (int): The size of the square, defaults to 0.
        __position (tuple): The position of the square, defaults to (0, 0).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes Square with a size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).
        """
        self.size = size  # Sets the size of the square.
        self.position = position  # Sets the position of the square.

    @property
    def size(self):
        """
        Returns the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size  # Returns the size of the square.

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):  # Checks if value is an integer.
            raise TypeError("size must be an integer")
        if value < 0:  # Checks if value is >= 0.
            raise ValueError("size must be >= 0")
        self.__size = value  # Sets the new size of the square.

    @property
    def position(self):
        """
        Returns the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position  # Returns the position of the square.

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        # Checks if value is a tuple of 2 positive integers.
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Sets the new position of the square.

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2  # Calculates and returns the area.

    def my_print(self):
        """
        Prints the square using '#' character at its position.
        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:  # Checks if size is 0.
            print()  # Prints an empty line.
        else:
            for _ in range(self.__position[1]):
                print()  # Prints spaces for vertical position.
            for _ in range(self.__size):
                # Prints the square at its position.
                print(" " * self.__position[0] + "#" * self.__size)
