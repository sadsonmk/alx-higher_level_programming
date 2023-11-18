#!/usr/bin/python3
"""This is a script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State, Session
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306
    state_name = "Louisiana"

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(user,
                           password, port, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)
    session.add(State(name=state_name))
    session.commit()
    res = session.query(State).filter(State.name == state_name).first()
    print(res.id)
