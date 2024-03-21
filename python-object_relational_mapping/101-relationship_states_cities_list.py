#!/usr/bin/python3
"""
Module: 101-relationship_states_cities_list.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script lists all State objects, and corresponding City objects, contained in
the database hbtn_0e_101_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id and cities.id.
Results are displayed as they are in the example below.
The code is not executed when imported.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


def list_states_cities():
    """
    Function to list all State objects, and corresponding City objects.
    """

    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py "
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

        query = session.query(State).order_by(State.id)

        for state in query:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))

    except Exception as e:
        print(e)

    finally:
        if session:
            session.close()


if __name__ == "__main__":
    list_states_cities()
