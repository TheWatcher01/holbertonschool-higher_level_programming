#!/usr/bin/python3
"""
Module: check_MySQL.py
Author: TheWatcher01
Date: 21/03/2024
Description:
This module provides a function to check if the MySQL service is running,
and starts it if it is not.
"""

# Import necessary modules
import subprocess


def check_mysql():
    """
    Function to check if the MySQL service is running, and start it if not.
    """

    try:
        # Check if the MySQL service is running
        subprocess.check_output('service mysql status', shell=True)
    except subprocess.CalledProcessError:
        # If the MySQL service is not running, start it
        print("MySQL is not running. Starting MySQL...")
        subprocess.run('service mysql start', shell=True)
