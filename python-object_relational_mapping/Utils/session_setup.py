#!/usr/bin/python3
"""
Module: session_setup.py
Author: TheWatcher01
Date: 21/03/2024
Description:
This module provides a function to setup the SQLAlchemy session.
It takes 1 argument: SQLAlchemy engine.
Function creates a session using the provided engine.
The code is not executed when imported.
"""

# Import necessary modules
from sqlalchemy.orm import sessionmaker


def setup_session(engine):
    """
    Function to setup the SQLAlchemy session.
    """

    # Initialize session to None
    session = None

    try:
        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a Session
        session = Session()

    except Exception as e:
        # Print the full exception
        print(e)

    return session
