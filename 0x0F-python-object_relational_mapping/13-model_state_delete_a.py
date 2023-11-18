#!/usr/bin/python3
"""This is a script that deletes all State objects
    with a name containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State, Session
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(user,
                           password, port, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)
    states = session.query(State).filter(State.name.contains('a')).all()

    for state in states:
        session.delete(state)
    session.commit()
