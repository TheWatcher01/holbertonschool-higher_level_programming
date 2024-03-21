#!/usr/bin/python3
"""
Module: 12-model_state_update_id_2.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script changes the name of a State object from the database hbtn_0e_6_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
Changes the name of the State where id = 2 to New Mexico.
The code is not executed when imported.
"""

# Import necessary modules
from sqlalchemy.orm import sessionmaker
from Utils.check_MySQL import check_mysql
from Utils.engine_setup import setup_engine
from model_state import Base, State
import sys


def update_state():
    """
    Function to update the name of a State object in the database.
    """

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py "
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

        # Query the database for the State object with id = 2
        state = session.query(State).get(2)

        # Update the name of the State object
        if state is not None:
            state.name = "New Mexico"

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
    update_state()
