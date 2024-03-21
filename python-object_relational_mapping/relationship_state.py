#!/usr/bin/python3
"""
Module: relationship_state.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Contains the class definition of States and an instance Base.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class definition for State.
    """

    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete")

    def __str__(self):
        """
        String representation of the class.
        """
        return "{}: {}".format(self.id, self.name)
