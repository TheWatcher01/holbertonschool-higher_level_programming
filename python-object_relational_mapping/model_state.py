#!/usr/bin/python3
"""
Module: model_state.py
Author: TheWatcher01
Date: 21/03/2024
Description:
Defines the class State and an instance Base.
"""

# Import necessary modules
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class
Base = declarative_base()


class State(Base):
    """
    Class that inherits from Base and links to the MySQL table states.
    """

    # Link to the MySQL table states
    __tablename__ = 'states'

    # Class attribute 'id' that represents a column of an auto-generated,
    # unique integer, can’t be null and is a primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Class attribute 'name' that represents a column of a string with maximum
    # 128 characters and can’t be null
    name = Column(String(128), nullable=False)
