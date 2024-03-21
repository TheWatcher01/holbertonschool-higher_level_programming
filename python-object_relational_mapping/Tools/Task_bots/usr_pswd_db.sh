#!/bin/bash

# Prompt the user for their database credentials
read -p "Enter your database username: " username
read -sp "Enter your database password: " password
read -p "Enter your database name: " database

# Export the credentials as environment variables
export DB_USER=$username
export DB_PASS=$password
export DB_NAME=$database

# Run your Python script and capture its output
output=$(python3 0-select_states.py)

# Check if the output contains the expected database name
if [[ $output == *"$database"* ]]; then
    echo "Successfully connected to the database."
else
    echo "Failed to connect to the database."
fi
