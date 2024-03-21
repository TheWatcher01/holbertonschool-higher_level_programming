#!/usr/bin/python3
"""
Module: 4-cities_by_state.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script lists all cities from the database hbtn_0e_4_usa.
It takes 3 arguments: mysql username, mysql password and database name.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id and displayed as they are.
The code is not executed when imported.
"""

# Import necessary modules
from Utils.check_MySQL import check_mysql
from Utils.engine_setup import setup_engine
from Utils.session_setup import setup_session
from model_state import Base, State
from model_city import City
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
        # Create an engine
        engine = setup_engine(username, password, database)

        # Check if engine was successfully created
        if engine is None:
            return

        # Create a Session
        session = setup_session(engine)

        # Query the database for all cities and their states
        cities = session.query(City, State).join(State).order_by(City.id)

        # Check if any City objects were found
        if cities.count() > 0:
            for city, state in cities:
                print("{}: ({}) {}".format(state.name, city.id, city.name))
        else:
            print("Not found")

    except Exception as e:
        # Print the full exception
        print(e)

    finally:
        # Close the Session
        if session:
            session.close()


# Ensure the script is not executed when imported
if __name__ == "__main__":
    check_mysql()
    list_cities()
