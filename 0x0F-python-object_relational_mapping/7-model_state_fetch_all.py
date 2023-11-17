#!/usr/bin/python3
"""This is a script that lists all State objects
    from the database hbtn_0e_6_usa using SQLAlchemy"""

import sys
from model_state import Base, State, Session
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
                           user, password, port, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)
    for state in session.query(State).order_by(State.id).all():
        print('{}: {}'.format(state.id, state.name))

    session.close()
