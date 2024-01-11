#!/usr/bin/python3
""" This module is to create a state model """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb


mymetada = MetaData()
Base = declarative_base(metadata=mymetada)


class State(Base):
    """creation of the table states"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
