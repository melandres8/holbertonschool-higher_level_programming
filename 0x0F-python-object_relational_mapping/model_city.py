#!/usr/bin/python3
""" City script """
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ City class method """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement="auto",
    )
    name = Column(
        String(128),
        nullable=False,
    )
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False,
    )
