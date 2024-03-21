#!/usr/bin/env python3
import MySQLdb
import os


def connect_to_database():
    return MySQLdb.connect(host="localhost", port=3306,
                           user=os.getenv('DB_USER'), passwd=os.getenv('DB_PASS'), db=os.getenv('DB_NAME'))


def get_all_states(cur):
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    return cur.fetchall()


def get_states_starting_with_n(cur):
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    return cur.fetchall()
