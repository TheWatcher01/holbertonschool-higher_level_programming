#!/usr/bin/python3
"""
Module: 3-my_safe_filter_states.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script lists all states with specific name from database hbtn_0e_0_usa.
It takes 4 arguments: mysql username, mysql password, database name,
and the state name to be searched.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id and displayed as they are.
The code is not executed when imported.
"""

# Import necessary modules
from Utils.check_MySQL import check_mysql
from Utils.engine_setup import setup_engine
from Utils.session_setup import setup_session
from model_state import Base, State
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
        # Create an engine
        engine = setup_engine(username, password, database)

        # Check if engine was successfully created
        if engine is None:
            return

        # Create a Session
        session = setup_session(engine)

        # Query the database for the State object with the given name
        states = session.query(State).filter(
            State.name == state_name_searched).order_by(State.id)

        # Check if any State objects were found
        if states.count() > 0:
            for state in states:
                print("{}: {}".format(state.id, state.name))
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
    filter_states()
