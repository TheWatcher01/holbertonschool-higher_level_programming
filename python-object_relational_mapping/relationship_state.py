#!/usr/bin/python3
'''
Contains the class def of States and an instance
Base = declarative_base()
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''Class def for State'''

    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City",
                          cascade="all")

    def __str__(self):
        '''str form of the class'''
        return "{}: {}".format(self.id, self.name)
