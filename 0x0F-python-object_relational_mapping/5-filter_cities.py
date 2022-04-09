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
    output = []
    for row in query_rows:
        if row[1] == sys.argv[4]:
            output.append(row[0])
    print(*output, sep=', ')
    cur.close()
    db.close()
