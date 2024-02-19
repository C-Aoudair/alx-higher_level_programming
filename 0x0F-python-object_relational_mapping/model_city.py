#!/usr/bin/python3
"""Dfines a City model"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """Represent a cities table in MySQL database"""

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    """state = relationship("State", back_populates="city")"""
