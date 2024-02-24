#!/usr/bin/python3
"""
Module defining BaseGeometry and Rectangle classes.

BaseGeometry provides basic validation for geometric properties.
Rectangle, subclass of BaseGeometry, include propertie specific to rectangle.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inheriting from BaseGeometry.

    Attributes:
        __width (int): Width of rectangle, must be integer greater than 0.
        __height (int): Height of rectangle, must be integer greater than 0.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with validated width and height.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        # Validate and set width
        self.__width = self.integer_validator("width", width)

        # Validate and set height
        self.__height = self.integer_validator("height", height)
