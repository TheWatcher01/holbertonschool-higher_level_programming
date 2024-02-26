#!/usr/bin/python3
"""
This script demonstrates the process of creating, manipulating, and persisting a Student object.

It imports necessary modules and classes, creates a Student instance, and then performs operations such as
saving it to a file, reading from a file, and updating the instance based on the saved data.
"""

import os
import sys

# Importing necessary classes and functions from modules
Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]  # Path for the file to save to

# Remove the file if it already exists
if os.path.exists(path):
    os.remove(path)

# Create a new Student instance and display its details
student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

# Save the student's JSON representation to a file
save_to_json_file(j_student_1, path)
read_file(path)
print("\nSaved to disk")

# Create a fake student and display its details
print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

# Load the student data from the file and update the fake student
print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

# Update the attributes of new_student_1 with the data from j_student_1
new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
