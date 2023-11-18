#!/usr/bin/python3
"""This is a script that changes the name
    of a State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State, Session
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306
    new_name = "New Mexico"

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(user,
                           password, port, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)
    state = session.query(State).filter(State.id == 2).one()
    state.name = new_name
    session.add(state)
    session.commit()
