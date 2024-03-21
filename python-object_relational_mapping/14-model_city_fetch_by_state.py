#!/usr/bin/python3
"""
Module: 14-model_city_fetch_by_state.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script prints all City objects from the database hbtn_0e_14_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id.
Results are displayed as they are in the example below
(<state name>: (<city id>) <city name>).
The code is not executed when imported.
"""

from sqlalchemy.orm import sessionmaker
from Utils.check_MySQL import check_mysql
from Utils.engine_setup import setup_engine
from model_state import Base, State
from model_city import City
import sys


def fetch_cities():
    """
    Function to print all City objects from the database.
    """

    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py "
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

        query = session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id)

        for state, city in query:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

    except Exception as e:
        print(e)

    finally:
        if session:
            session.close()


if __name__ == "__main__":
    check_mysql()
    fetch_cities()
