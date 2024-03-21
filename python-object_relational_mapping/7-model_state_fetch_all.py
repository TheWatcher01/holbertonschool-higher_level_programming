#!/usr/bin/python3
"""
Module: 7-model_state_fetch_all.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Script lists all State objects from the database hbtn_0e_6_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
Uses SQLAlchemy to connect to MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id and displayed as they are.
The code is not executed when imported.
"""

# Import necessary modules
from check_MySQL import check_mysql
from db_config import get_database_session
from db_ops import list_states
import sys

if __name__ == "__main__":
    check_mysql()
    session = get_database_session(sys.argv[1], sys.argv[2], sys.argv[3])
    try:
        list_states(session)
    except Exception as e:
        print(e)
    finally:
        if session:
            session.close()
