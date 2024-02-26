#!/usr/bin/python3
"""
Script facilitates storage and retrieval of command-line
arguments in JSON file.
It imports necessary modules and functions, checks for existence
of JSON file,
reads data from it if available, and appends new command-line
arguments to file.
"""

import os
import sys
import json

# Import custom functions for JSON file operations
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Check if 'add_item.json' exists and is not empty
if os.path.exists("add_item.json") and os.path.getsize("add_item.json") > 0:
    # Load existing data from 'add_item.json'
    items = load_from_json_file("add_item.json")
else:
    # Initialize an empty list if the file doesn't exist or is empty
    items = []

# Extend the list with command-line arguments, excluding the script name
items.extend(sys.argv[1:])

# Save the updated list back to 'add_item.json'
save_to_json_file(items, "add_item.json")
