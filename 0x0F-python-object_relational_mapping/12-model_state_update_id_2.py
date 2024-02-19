#!/usr/bin/python3
""" changes the name of a State object from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    with Session() as session:

        myState = session.query(State).filter(State.id == 2).first()
        myState.name = "New Mexico"
        session.commit()
