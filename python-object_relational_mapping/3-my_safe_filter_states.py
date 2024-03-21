#!/usr/bin/python3
"""
Module: 3-my_safe_filter_states.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script lists all states with specific name from database hbtn_0e_0_usa.
It takes 4 arguments: mysql username, mysql password, database name,
and the state name to be searched.
Uses MySQLdb to connect to MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id and displayed as they are.
The code is not executed when imported.
"""

# Import necessary modules
from check_MySQL import check_mysql
import MySQLdb
import sys


def filter_states():
    """
    Function to filter states based on user input.
    """

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py username password "
              "database state_name_searched")
        return

    # Retrieve the arguments passed to the script
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]

    try:
        # Connect to the database
        db = MySQLdb.connect(host="localhost",
                             user=username,
                             passwd=password,
                             db=database,
                             port=3306)

        # Create a cursor object
        cur = db.cursor()

        # Execute the SQL query
        query = ("SELECT * FROM states WHERE name = %s "
                 "ORDER BY id ASC")
        cur.execute(query, (state_name_searched,))

        # Retrieve and display the results
        for row in cur.fetchall():
            print(row)

    except MySQLdb.Error as e:
        # Print any error that occurs
        print(f"Error: {str(e)}")

    finally:
        # Close the connection and cursor
        if cur:
            cur.close()
        if db:
            db.close()


# Ensure the script is not executed when imported
if __name__ == "__main__":
    check_mysql()
    filter_states()
