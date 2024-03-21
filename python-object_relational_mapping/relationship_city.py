#!/usr/bin/python3
"""
Module: relationship_city.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Contains the class definition of City and an instance Base.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    Class definition for City.
    """

    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)

    def __str__(self):
        """
        String representation of the class.
        """
        return "{}: {}".format(self.id, self.name)
