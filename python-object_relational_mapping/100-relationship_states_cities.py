#!/usr/bin/python3
"""
Module: 100-relationship_states_cities.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script creates the State “California” with the City “San Francisco” from the
database hbtn_0e_100_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
The code is not executed when imported.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def relationship_state():
    """
    Function to create the State “California” with the City “San Francisco”.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1],
                                  argv[2],
                                  argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    session.add(State(name='California', cities=[City(name='San Francisco')]))
    session.commit()
    session.close()


if __name__ == "__main__":
    relationship_state()
