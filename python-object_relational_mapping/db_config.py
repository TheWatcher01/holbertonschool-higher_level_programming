#!/usr/bin/python3
"""
Module: db_config.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Module provides a function to create a database session.
"""

# Import necessary modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_database_session(username, password, database):
    """
    Function to create a database session.
    Takes 3 arguments: mysql username, mysql password, and database name.
    Returns a Session object.
    """

    # Create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create and return a Session
    return Session()
