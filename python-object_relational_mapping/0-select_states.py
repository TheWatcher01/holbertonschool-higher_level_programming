#!/usr/bin/python3
"""
Module for interacting with a MySQL database.
"""

import os
import sys
import MySQLdb
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import OperationalError

# Define a base class for declarative models
Base = declarative_base()


class State(Base):
    """
    Define a State model that includes `id` and `name` fields.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String)


def select_states():
    """
    Connects to MySQL server, creates database and table if they don't exist,
    inserts data into table, and then queries and prints all rows from table.
    """
    # Get database credentials from environment variables
    username = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    database = os.getenv('DB_NAME')

    try:
        # Connect to the MySQL server with MySQLdb
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password)
        cur = db.cursor()

        # Execute SQL queries to set up the database and table
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {database};")
        cur.execute(f"USE {database};")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS states (
                id INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(256) NOT NULL,
                PRIMARY KEY (id)
            );
        """)
        cur.execute("""
            INSERT INTO states (name)
            VALUES ("California"), ("Arizona"), ("Texas"), ("New York"),
                    ("Nevada");""")

        # Create an SQLAlchemy engine that connects to the MySQL server
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database}')

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a Session
        session = Session()

        # Query the database and print each row
        for state in session.query(State).order_by(State.id):
            print(state.id, state.name)

        # Close the Session to free up resources
        session.close()

    except OperationalError as e:
        if "Access denied for user" in str(e):
            print("Invalid username or password.")
            sys.exit(1)
        elif "Unknown database" in str(e):
            print("Unknown database.")
            sys.exit(1)
        else:
            print("An error occurred.")
            sys.exit(1)


# Only run following code when this file is run directly not when it's imported
if __name__ == "__main__":
    select_states()
