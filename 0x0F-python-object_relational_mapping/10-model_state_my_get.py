#!/usr/bin/python3
"""This is a script that prints the State object
    with the name passed as argument from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State, Session
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    port = 3306

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(user,
                           password, port, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    state = session.query(State).filter(State.name == state).all()

    if state:
        for res in state:
            print('{}'.format(res.id))
    else:
        print('Not found')

    session.close()
