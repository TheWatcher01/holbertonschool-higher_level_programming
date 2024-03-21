#!/usr/bin/python3
"""
Module: 8-model_state_fetch_first.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script prints the first State object from the database hbtn_0e_6_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
The state displayed is the first in states.id.
The code is not executed when imported.
"""

# Import necessary modules
from Utils.check_MySQL import check_mysql
from Utils.engine_setup import setup_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


def fetch_first_state():
    """
    Function to print the first State object from the database.
    """

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py username password "
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

        # Check if engine was successfully created
        if engine is None:
            return

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a Session
        session = Session()

        # Query the database for the first State object
        state = session.query(State).order_by(State.id).first()

        # Check if a State object was found
        if state is not None:
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")

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
    fetch_first_state()
