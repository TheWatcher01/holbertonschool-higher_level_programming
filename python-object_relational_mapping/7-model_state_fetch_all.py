#!/usr/bin/python3
"""
Module: 7-model_state_fetch_all.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script lists all State objects from the database hbtn_0e_6_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id and displayed as they are.
The code is not executed when imported.
"""

# Import necessary modules
from Utils.check_MySQL import check_mysql
from Utils.engine_setup import setup_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


def list_states():
    """
    Function to list all State objects from the database.
    """

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py username password "
              "database")
        return

    # Retrieve the arguments passed to the script
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Initialize session to None
    session = None

    try:
        # Create an engine
        engine = setup_engine(username, password, database)

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a Session
        session = Session()

        # Query the database
        for state in session.query(State).order_by(State.id):
            print("{}: {}".format(state.id, state.name))

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
    list_states()
