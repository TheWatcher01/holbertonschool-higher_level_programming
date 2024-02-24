#!/usr/bin/python3
"""
Script demonstrate process of creating instance of MyClass, modifying its state
and converting it to dictionary representation using the class_to_json function
"""

# Importing MyClass and class_to_json from their respective files
MyClass = __import__('8-my_class_2').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

# Creating an instance of MyClass and updating its state
m = MyClass("John")
m.win()  # Increment the score
print(type(m))  # Display the type of the MyClass instance
print(m)  # Display the current state of the MyClass instance

# Converting the MyClass instance to a dictionary
mj = class_to_json(m)
print(type(mj))  # Display the type of the resulting dictionary
print(mj)  # Display the dictionary representation of the MyClass instance
