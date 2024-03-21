#!/usr/bin/python3
"""
Module: 1-filter_states.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script lists all states with name starting with N (upper N) from
database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password and database name.
It uses module MySQLdb to connect to a MySQL server running on localhost
at port 3306.
Results are sorted in ascending order by states.id and displayed as they are.
The code is not executed when imported.
"""
from check_MySQL import check_mysql
import MySQLdb
import sys


def filter_states():
    """
    Function to filter states based on user input.
    """

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py username password "
              "database")
        return

    # Retrieve the arguments passed to the script
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                    "ORDER BY id ASC")

        # Retrieve and display the results
        for row in cur.fetchall():
            print(row)

    except MySQLdb.Error as e:
        # Print any error that occurs
        print(e)

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
