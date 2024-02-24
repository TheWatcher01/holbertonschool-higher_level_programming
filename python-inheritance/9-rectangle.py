#!/usr/bin/python3

"""
This module provides a Rectangle class that inherits from BaseGeometry.
It includes methods for initializing a rectangle with width and height,
calculating its area, and obtaining a string representation of the rectangle.

Classes:
    Rectangle: Inherits from BaseGeometry and represents a rectangle.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (int): Width of rectangle, must be positive integer.
            height (int): Height of rectangle, must be positive integer.
        """
        self.integer_validator("width", width)  # Validate width
        self.__width = width  # Set width
        self.integer_validator("height", height)  # Validate height
        self.__height = height  # Set height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height  # Return area (width * height)

    def __str__(self):
        """
        Provide a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        # Rectangle description
        return f"[Rectangle] {self.__width}/{self.__height}"
