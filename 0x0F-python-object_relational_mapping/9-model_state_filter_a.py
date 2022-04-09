#!/usr/bin/python3
"""
script that lists all State objects that contain the letter "a"
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
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
    Base.metadata.create_all(engine)

    session = Session(engine)
    objectState = session.query(State).all()
    for state in objectState:
        if "a" in state.name:
            print(f"{state.id}: {state.name}")
    session.close()
