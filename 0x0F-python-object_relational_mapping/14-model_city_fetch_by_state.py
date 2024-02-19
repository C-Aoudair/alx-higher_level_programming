#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

if __name__ == "__main__":
    from model_city import City
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)

    session = Session()
    cities = session.query(City).all()

    for city in cities:
        stateName = (
            session.query(State.name)
            .filter(State.id == city.state_id)
            .scalar()
            )

        print(f"{stateName}: ({city.id}) {city.name}")
