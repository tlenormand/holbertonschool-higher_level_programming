#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    session = Session(engine)
    query = session.query(
        City,
        State
    ).filter(
        City.state_id == State.id
    ).order_by(
        City.id
    ).all()
    for city, state in query:
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
