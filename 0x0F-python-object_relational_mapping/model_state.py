#!/usr/bin/python3
'''class definition of State'''
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class State(Base):
    '''Class that inherits from Base class.'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
