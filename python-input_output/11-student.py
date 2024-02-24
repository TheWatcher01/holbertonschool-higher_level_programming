#!/usr/bin/python3
"""
Module defines Student class with additional functionality to
reload its attributes from JSON object.
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

    def to_json(self, attrs=None):
        """
        Converts specified attributes of Student instance into dictionary.

        Args:
            attrs (list, optional): List of attribute names to include in
                                    resulting dictionary.
                                    If None, all attributes are included.

        Returns:
            dict: A dictionary containing key/value pairs of attributes.
        """
        if attrs is None:
            # Return all attributes if no specific attrs provided
            return self.__dict__
        # Return only specified attributes
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """
        Updates attributes of Student instance based on key/value pairs
        in provided JSON object.

        Args:
            json (dict): Dictionary representing JSON object with key/value
            pairs to update instance's attributes.
        """
        for k, v in json.items():
            # Set each attribute to corresponding value from JSON object
            setattr(self, k, v)
