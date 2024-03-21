"""
Module: db_ops.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Module provides a function to list all State objects from database.
"""

# Import necessary modules
from model_state import State


def list_states(session):
    """
    Function to list all State objects from the database.
    Takes 1 argument: session (SQLAlchemy Session object).
    Prints the id and name of each State object, sorted by id.
    """

    # Query the database
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
