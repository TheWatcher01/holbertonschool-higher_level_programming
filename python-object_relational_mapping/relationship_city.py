#!/usr/bin/python3
"""
Module: relationship_state.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Python file that contains the class definition of a State.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    State class:
    - inherits from Base
    - links to the MySQL table states
    - class attribute id that represents a column of an auto-generated,
      unique integer, can’t be null and is a primary key
    - class attribute name that represents a column of a string of 128
      characters and can’t be null
    - class attribute cities must represent a relationship with the class City
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete")
