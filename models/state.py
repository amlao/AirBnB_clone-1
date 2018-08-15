#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
import os
import models


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        city = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        """
            a public getter for cities
        """
        return [city for city in State.cities if city.state_id == self.id]
