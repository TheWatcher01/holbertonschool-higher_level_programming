#!/usr/bin/python3
"""
Module defines Student class, which includes method for converting
its attributes to a dictionary representation.
"""


class Student:
    """
    A class to represent a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        The constructor for Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name  # Assign the first name
        self.last_name = last_name    # Assign the last name
        self.age = age                # Assign the age

    def to_json(self):
        """
        Converts the Student instance into a dictionary.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        return self.__dict__  # Return the dictionary of the class attributes
