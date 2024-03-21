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

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


def create_state_city():
    """
    Function to create the State “California” with the City “San Francisco”.
    """

    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py "
              "username password database")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name="California")
        new_city = City(name="San Francisco", state=new_state)

        session.add(new_state)
        session.add(new_city)
        session.commit()

    except Exception as e:
        print(e)

    finally:
        if session:
            session.close()


if __name__ == "__main__":
    create_state_city()
