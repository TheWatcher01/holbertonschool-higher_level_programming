#!/usr/bin/python3
"""
Script demonstrates usage of MyClass and class_to_json functionalities.

Imports MyClass & class_to_json from their respective modules, creates instance
of MyClass, updates its state, and then converts it to a JSON-like dictionary.
"""

# Import MyClass and class_to_json from their respective modules
MyClass = __import__('8-my_class_2').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

# Create an instance of MyClass and update its state
m = MyClass("John")
m.win()
print(type(m))  # Print the type of the MyClass instance
print(m)  # Print the MyClass instance

# Convert the MyClass instance to a JSON-like dictionary
mj = class_to_json(m)
print(type(mj))  # Print the type of the resulting dictionary
print(mj)  # Print the dictionary
