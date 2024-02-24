#!/usr/bin/python3
"""
Script demonstrates the creation of multiple Student instances and how to
convert each of them into a dictionary representation using the to_json method.
"""

# Import the Student class from the '9-student' module
Student = __import__('9-student').Student

# Create a list of Student instances
students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

# Iterate through each student and print their JSON representation
for student in students:
    j_student = student.to_json()  # Convert the student to a dictionary
    print(type(j_student))  # Print the type of the dictionary
    print(j_student['first_name'])  # Access and print the first name
    print(type(j_student['first_name']))  # Print the type of the first name
    print(j_student['age'])  # Access and print the age
    print(type(j_student['age']))  # Print the type of the age
