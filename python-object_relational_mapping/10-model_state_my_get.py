#!/usr/bin/python3
"""
Module: 10-model_state_my_get.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script prints the State object with the name passed as argument from the
database hbtn_0e_6_usa.
It takes 4 arguments: mysql username, mysql password, database name, and state
name to search.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
The code is not executed when imported.
"""

# Import necessary modules
from Utils.check_MySQL import check_mysql
from Utils.engine_setup import setup_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


def get_state():
    """
    Function to print the State object with the name passed as argument from
    the database.
    """

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py username password database "
              "state_name")
        return

    # Retrieve the arguments passed to the script
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

        # Query the database for the State object with the given name
        state = session.query(State).filter(State.name == state_name).first()

        # Check if a State object was found
        if state is not None:
            print(state.id)
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
    get_state()
