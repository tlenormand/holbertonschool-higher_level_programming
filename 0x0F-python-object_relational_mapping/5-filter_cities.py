#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
from turtle import st
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host=("localhost"),
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute(
        ("SELECT cities.name, states.name \
        FROM cities \
        INNER JOIN states \
        ON cities.state_id = states.id")
        )

    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query_rows))
    cur.close()
    db.close()
