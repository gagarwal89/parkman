from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

m1 = Movie("Robocop", 1987)
m1.director = Director("Paul Verhoeven")

d2 = Director("George Lucas")
d2.movies = [Movie("Star Wars", 1977), Movie("THX 1138", 1971)]

try:
    session.add(m1)
    session.add(d2)
    session.commit()
except:
    session.rollback()