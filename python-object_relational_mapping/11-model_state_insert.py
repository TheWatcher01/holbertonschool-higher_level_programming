#!/usr/bin/python3
"""
Module: 11-model_state_insert.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script adds the State object “Louisiana” to the database hbtn_0e_6_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
Prints the new states.id after creation.
The code is not executed when imported.
"""

# Import necessary modules
from sqlalchemy.orm import sessionmaker
from Utils.check_MySQL import check_mysql
from Utils.engine_setup import setup_engine
from model_state import Base, State
import sys


def add_state():
    """
    Function to add the State object “Louisiana” to the database.
    """

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py username password database")
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
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create a new State object
        new_state = State(name="Louisiana")

        # Add the new State object to the session
        session.add(new_state)

        # Commit the transaction
        session.commit()

        # Print the id of the new State object
        print(new_state.id)

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
    add_state()
