#!/usr/bin/python3
"""
Module: 102-relationship_cities_states_list.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script lists all City objects from the database hbtn_0e_101_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id.
Results are displayed as they are in the example below.
The code is not executed when imported.
"""

from sqlalchemy.orm import sessionmaker
from Utils.check_MySQL import check_mysql
from Utils.engine_setup import setup_engine
from relationship_state import Base, State
from relationship_city import City
import sys


def list_cities():
    """
    Function to list all City objects.
    """

    if len(sys.argv) != 4:
        print("Usage: ./102-relationship_cities_states_list.py "
              "username password database")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        engine = setup_engine(username, password, database)

        if engine is None:
            return

        Session = sessionmaker(bind=engine)
        session = Session()

        query = session.query(City).order_by(City.id)

        for city in query:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    except Exception as e:
        print(e)

    finally:
        if session:
            session.close()


if __name__ == "__main__":
    check_mysql()
    list_cities()
