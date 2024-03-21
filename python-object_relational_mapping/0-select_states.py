#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
from check_MySQL import check_mysql
import MySQLdb
from sys import argv

if __name__ == "__main__":
    check_mysql()
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
