import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    height = Column(Integer)
    gender = Column(String(250))
    eye_color = Column(String(250))

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250))
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)

    user = relationship(User)


class FavouriteCharacters(Base):
    __tablename__ = 'FavouriteCharacters'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship(User)

    character_id = Column(Integer, ForeignKey('Characters.id'))
    character = relationship(Characters)
    

class FavouritePlanets(Base):
    __tablename__ = 'FavouritePlanets'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("Users.id"))
    user = relationship(User)

    planet_id = Column(Integer, ForeignKey("Planets.id"))
    planet = relationship(Planets)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
