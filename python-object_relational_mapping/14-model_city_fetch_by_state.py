#!/usr/bin/python3
"""Imprime tous les objets de la ville de la bdd hbtn_0e_14_usa"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, passwd, database = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city, state in session.query(
            City, State).join(State).order_by(City.id.asc()).all():
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
