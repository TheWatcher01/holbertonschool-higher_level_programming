#!/usr/bin/python3
"""
Module: engine_setup.py
Author: TheWatcher01
Date: 21/03/2024
Description:
This module provides a function to setup the SQLAlchemy engine.
It takes 3 arguments: mysql username, mysql password, and database name.
Function creates engine that connects to MySQL server running on
localhost at port 3306.
The code is not executed when imported.
"""
from sqlalchemy import create_engine


def setup_engine(username, password, database):
    """
    Function to setup the SQLAlchemy engine.
    """

    try:
        # Create an engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)
    except Exception as e:
        print("Error while creating the engine: ", e)
        return None

    return engine
