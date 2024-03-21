#!/usr/bin/python3
"""
Module: model_city.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Python file that contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city for a MySQL database.

    Attributes:
        id (int): an auto-generated, unique integer
                  representing the city's ID.
        name (str): a string with a maximum of
                    128 characters representing the city's name.
        state_id (int): an integer representing the state's ID
                        that the city belongs to.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(
        'states.id', ondelete="CASCADE"), nullable=False)
