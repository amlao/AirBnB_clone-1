#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from os import getenv, environ
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
