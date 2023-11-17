#!/usr/bin/python3
"""This is a python file that contains the class definition
    of a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
Session = sessionmaker()


class State(Base):
    """class State which inherits from the Base"""
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
