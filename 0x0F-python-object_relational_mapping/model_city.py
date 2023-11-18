#!/usr/bin/python3
"""This is a python file that contains the class definition
    of a City and an instance Base = declarative_base()
    class City inherits from Base
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State

Base = declarative_base()
Session = sessionmaker()


class City(Base):
    """class City which inherits from the Base"""
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), nullable=False, ForeignKey('states.id')
