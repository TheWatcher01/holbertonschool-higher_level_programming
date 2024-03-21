#!/usr/bin/python3
"""
Module: relationship_city.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Python file that contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
