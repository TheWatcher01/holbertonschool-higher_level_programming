#!/usr/bin/python3
"""
Module: 4-cities_by_state.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script lists all cities from the database hbtn_0e_4_usa.
It takes 3 arguments: mysql username, mysql password and database name.
Uses MySQLdb to connect to MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id and displayed as they are.
The code is not executed when imported.
"""

# Import necessary modules
from Utils.check_MySQL import check_mysql
import MySQLdb
import sys


def list_cities():
    """
    Function to list all cities from the database.
    """

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py username password "
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
        cur.execute("""SELECT cities.id, cities.name, states.name
                       FROM cities
                       JOIN states ON cities.state_id = states.id
                       ORDER BY cities.id ASC""")

        # Retrieve and display the results
        for row in cur.fetchall():
            print(row)

    except MySQLdb.Error as e:
        # Print the full exception
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
    list_cities()
