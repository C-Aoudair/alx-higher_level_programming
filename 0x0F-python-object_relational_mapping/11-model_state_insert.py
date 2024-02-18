#!/usr/bin/python3
""" adds the State object “Louisiana” to the databasehbtn_0e_6_usa"""

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

        newState = State(name="Louisiana")
        session.add(newState)
        session.commit()
        print(newState.id)
