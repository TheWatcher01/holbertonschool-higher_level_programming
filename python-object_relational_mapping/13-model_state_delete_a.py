#!/usr/bin/python3
"""
Module: 13-model_state_delete_a.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script deletes all State objects with a name containing the letter a from the
database hbtn_0e_6_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
The code is not executed when imported.
"""

# Import necessary modules
from sqlalchemy.orm import sessionmaker
from Utils.check_MySQL import check_mysql
from Utils.engine_setup import setup_engine
from model_state import Base, State
import sys


def delete_states():
    """
    Function to delete all State objects with a name containing the letter a.
    """

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py "
              "username password database")
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

        # Query the database for all State objects with a name containing 'a'
        states = session.query(State).filter(State.name.contains('a'))

        # Delete all State objects with a name containing 'a'
        for state in states:
            session.delete(state)

        # Commit the transaction
        session.commit()

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
    delete_states()
